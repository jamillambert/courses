use log::{debug, info};
use rand::prelude::*;
use rusty_engine::prelude::*;
use std::{f32::consts::PI, time::SystemTime};

struct GameState {
    high_score: i32,
    current_score: i32,
    frame_no: u32,
    measure_time: SystemTime,
    movement_speed: f32,
    barrel_index: i32,
    spawn_timer: Timer,
    max_barrels: i32,
    window_x: f32,
    window_y: f32,
}

impl Default for GameState {
    fn default() -> Self {
        Self {
            high_score: 10,
            current_score: 0,
            frame_no: 0,
            measure_time: SystemTime::now(),
            movement_speed: 100.0,
            barrel_index: 0,
            spawn_timer: Timer::from_seconds(1.0, true),
            max_barrels: 6,
            window_x: 0.0,
            window_y: 0.0,
        }
    }
}

fn reset_game(engine: &mut Engine, game_state: &mut GameState) {
    // When the game first starts or is over the score is reset to 0
    // and the player is moved back to the centre of the screen and
    // the movement speed reset

    // Set up of player
    engine.sprites.clear();
    let player = engine.add_sprite("player", SpritePreset::RacingCarBlue);
    player.translation = Vec2::new(0.0, 0.0);
    player.rotation = RIGHT;
    player.collision = true;

    // Creates 4 cars, one in each corner
    for i in 0..4 {
        let label = format!("car{}", i);
        let car = engine.add_sprite(label, SpritePreset::RacingCarYellow);
        let x_pos: i32 = (i / 2 * 2 - 1) * 300; // sets the positions to + and - 300
        let y_pos: i32 = (i % 2 * 2 - 1) * 150; // sets the positions to + and - 150
        car.translation = Vec2::new(x_pos as f32, y_pos as f32);
        car.collision = true;
    }

    // Set the current score to 0 and speed to 100
    game_state.current_score = 0;
    let score = engine.texts.get_mut("score").unwrap();
    score.value = format!("Score: {}", game_state.current_score);
    game_state.movement_speed = 100.0;
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {
    // Show current fps
    if game_state.frame_no == 0 {
        reset_game(engine, game_state);
    }
    if game_state.frame_no % 100 == 0 {
        output_debug_text(engine, game_state);
    }
    game_state.frame_no += 1;
    if game_state.window_x != engine.window_dimensions.x
        || game_state.window_y != engine.window_dimensions.y
    {
        resize_scoreboard(game_state, engine);
    }

    if let Some(labels) = in_collision(engine) {
        // Handles collisions of the player car
        if labels[0] == "player" {
            player_collision(&labels[1], engine, game_state);
        } else if labels[0].contains("b") {
            // if a barrel or bomb was spawned in collision with an NPC it is moved
            barrel_collision(engine, &labels[0], game_state);
        } else if labels[1].contains("b") {
            barrel_collision(engine, &labels[1], game_state);
        }
    }

    // Handles keyboard movement
    move_player(engine, game_state);
    loop_motion(engine);

    if game_state.spawn_timer.tick(engine.delta).just_finished() {
        spawn_barrel(engine, game_state);
    }
}

fn output_debug_text(engine: &mut Engine, game_state: &mut GameState) {
    let player = engine.sprites.get_mut("player").unwrap();
    let new_time = SystemTime::now();
    let fps = 100000
        / SystemTime::duration_since(&new_time, game_state.measure_time)
            .unwrap()
            .as_millis();
    game_state.measure_time = new_time;
    debug!(
        "Current score: {}, fps: {}, car x: {}, car y: {}",
        game_state.current_score, fps, player.translation.x, player.translation.y
    );
}

fn resize_scoreboard(game_state: &mut GameState, engine: &mut Engine) {
    // The window was resized
    game_state.window_x = engine.window_dimensions.x;
    game_state.window_y = engine.window_dimensions.y;
    // Move score text when the window is resized
    let score = engine.texts.get_mut("score").unwrap();
    score.translation.x = engine.window_dimensions.x / 2.0 - 80.0;
    score.translation.y = engine.window_dimensions.y / 2.0 - 30.0;
    let high_score = engine.texts.get_mut("high_score").unwrap();
    high_score.translation.x = -engine.window_dimensions.x / 2.0 + 100.0;
    high_score.translation.y = engine.window_dimensions.y / 2.0 - 30.0;
}

fn in_collision(engine: &mut Engine) -> Option<Vec<String>> {
    // If there is a collision the two sprite labels are returned, player is always
    // at location 0 if involved
    let mut labels = Vec::new();
    for event in engine.collision_events.drain(..) {
        debug!("{} is in collision with {}", event.pair.0, event.pair.1);
        if event.state == CollisionState::Begin {
            if event.pair.0 == "player" {
                labels.push(String::from("player"));
                labels.push(event.pair.1);
            } else if event.pair.1 == "player" {
                labels.push(String::from("player"));
                labels.push(event.pair.0);
            } else {
                labels.push(event.pair.0);
                labels.push(event.pair.1);
            }
            return Some(labels);
        }
    }
    return None;
}

fn barrel_collision(engine: &mut Engine, label: &String, game_state: &mut GameState) {
    let sprite = engine.sprites.get_mut(label).unwrap();
    (sprite.translation.x, sprite.translation.y) = randomise_location(game_state);
}

fn player_collision(label: &String, engine: &mut Engine, game_state: &mut GameState) {
    if label.contains("barrel") {
        // When the player hits a barrel they score 1 point and the barrel disappears
        info!("Player hit a barrel");
        engine.sprites.remove(label);
        game_state.current_score += 1;
        let score = engine.texts.get_mut("score").unwrap();
        score.value = format!("Score: {}", game_state.current_score);
        game_state.movement_speed += 50.0;
        if game_state.current_score > game_state.high_score {
            engine.audio_manager.play_sfx(SfxPreset::Jingle1, 0.5);
            game_state.high_score = game_state.current_score;
            info!("New High Score! {}", game_state.high_score);
            let high_score = engine.texts.get_mut("high_score").unwrap();
            high_score.value = format!("High Score: {}", game_state.high_score);
        } else {
            engine.audio_manager.play_sfx(SfxPreset::Minimize1, 0.5);
        }
    } else if label.contains("car") {
        // When the player hits another car or a bomb the game is over,
        // resetting the score and position
        engine.audio_manager.play_sfx(SfxPreset::Jingle3, 0.5);
        info!("Game Over!");
        reset_game(engine, game_state);
    }
}

fn spawn_barrel(engine: &mut Engine, game_state: &mut GameState) {
    // Creates a barrel after Timer has run and sets it to a random position on the screen
    // a maximum number of barrels are created and then exisiting ones are moved
    engine.audio_manager.play_sfx(SfxPreset::Click, 0.5);
    let label: String;
    let sprite_png: rusty_engine::sprite::SpritePreset;
    if game_state.barrel_index > game_state.max_barrels {
        game_state.barrel_index = 0;
        label = String::from("bomb");
        sprite_png = SpritePreset::RacingBarrelRed;
    } else {
        game_state.barrel_index += 1;
        label = format!("barrel{}", game_state.barrel_index);
        sprite_png = SpritePreset::RacingBarrelBlue;
    }
    let sprite = engine.add_sprite(&label, sprite_png);
    sprite.collision = true;
    (sprite.translation.x, sprite.translation.y) = randomise_location(game_state);
}

fn randomise_location(game_state: &mut GameState) -> (f32, f32) {
    // Returns a random location within the game screen, away 50 from the edges
    let max_x = game_state.window_x / 2.0 - 50.0;
    let max_y = game_state.window_y / 2.0 - 50.0;
    (
        thread_rng().gen_range(-max_x..max_x),
        thread_rng().gen_range(-max_y..max_y),
    )
}

fn move_player(engine: &mut Engine, game_state: &mut GameState) {
    // Handles the keyboard inputs to move the player sprite
    let player = engine.sprites.get_mut("player").unwrap();

    // first four cases are diagonal movement
    let diagonal_distance = game_state.movement_speed * engine.delta_f32 / 1.4142;
    // last four cases are orthogonal movement
    let distance = game_state.movement_speed * engine.delta_f32;
    if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Up, KeyCode::W])
        && engine
            .keyboard_state
            .pressed_any(&[KeyCode::Right, KeyCode::D])
    {
        player.rotation = PI / 4.0;
        player.translation.x += diagonal_distance;
        player.translation.y += diagonal_distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Up, KeyCode::W])
        && engine
            .keyboard_state
            .pressed_any(&[KeyCode::Left, KeyCode::A])
    {
        player.rotation = PI * 3.0 / 4.0;
        player.translation.x -= diagonal_distance;
        player.translation.y += diagonal_distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Down, KeyCode::S])
        && engine
            .keyboard_state
            .pressed_any(&[KeyCode::Left, KeyCode::A])
    {
        player.rotation = PI * 5.0 / 4.0;
        player.translation.x -= diagonal_distance;
        player.translation.y -= diagonal_distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Down, KeyCode::S])
        && engine
            .keyboard_state
            .pressed_any(&[KeyCode::Right, KeyCode::D])
    {
        player.rotation = PI * 7.0 / 4.0;
        player.translation.x += diagonal_distance;
        player.translation.y -= diagonal_distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Up, KeyCode::W])
    {
        player.rotation = UP;
        player.translation.y += distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Down, KeyCode::S])
    {
        player.rotation = DOWN;
        player.translation.y -= distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Left, KeyCode::A])
    {
        player.rotation = LEFT;
        player.translation.x -= distance;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Right, KeyCode::D])
    {
        player.rotation = RIGHT;
        player.translation.x += distance;
    }
}

fn loop_motion(engine: &mut Engine) {
    // Move the car to the other side of the window when it hits the edge
    let player = engine.sprites.get_mut("player").unwrap();
    if player.translation.x > engine.window_dimensions.x / 2.0 {
        player.translation.x = -engine.window_dimensions.x / 2.0 + 10.0;
        debug!(
            "The car moved off the screen, moved to x = {}",
            player.translation.x
        );
    } else if player.translation.x < -engine.window_dimensions.x / 2.0 {
        player.translation.x = engine.window_dimensions.x / 2.0 - 10.0;
        debug!(
            "The car moved off the screen, moved to x = {}",
            player.translation.x
        );
    }
    if player.translation.y > engine.window_dimensions.y / 2.0 {
        player.translation.y = -engine.window_dimensions.y / 2.0 + 10.0;
        debug!(
            "The car moved off the top of the screen, moved to y = {}",
            player.translation.y
        );
    } else if player.translation.y < -engine.window_dimensions.y / 2.0 {
        debug!(
            "The car moved off the screen, from y = {}",
            player.translation.y
        );
        player.translation.y = engine.window_dimensions.y / 2.0 - 10.0;
        debug!(
            "The car moved off the screen, moved to y = {}",
            player.translation.y
        );
    }
}

fn main() {
    // Starts a new game adds the game logic and runs the game state
    let mut game = Game::new();
    let game_state = GameState::default();

    let score = game.add_text("score", "Score: 0");
    score.translation = Vec2::new(-520.0, 320.0);

    let high_score = game.add_text(
        "high_score",
        format!("High Score: {}", game_state.high_score),
    );
    high_score.translation = Vec2::new(520.0, 320.0);

    // Play music and run the game
    game.audio_manager
        .play_music(MusicPreset::WhimsicalPopsicle, 0.1);
    game.add_logic(game_logic);
    game.run(game_state);
}
