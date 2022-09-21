use log::{debug, error, info, trace, warn};
use rand::prelude::*;
use rusty_engine::prelude::*;
use std::time::SystemTime;

struct GameState {
    high_score: i32,
    current_score: i32,
    frame_no: u32,
    measure_time: SystemTime,
    movement_speed: f32,
    barrel_index: i32,
    spawn_timer: Timer,
    move_timer: Timer,
    number_cars: i32,
    max_barrels: i32,
}

impl Default for GameState {
    fn default() -> Self {
        Self {
            high_score: 0,
            current_score: 0,
            frame_no: 0,
            measure_time: SystemTime::now(),
            movement_speed: 100.0,
            barrel_index: 0,
            spawn_timer: Timer::from_seconds(2.0, true),
            move_timer: Timer::from_seconds(0.09, true),
            number_cars: 4,
            max_barrels: 4,
        }
    }
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {
    // Show current fps
    if game_state.frame_no % 100 == 0 {
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
    game_state.frame_no += 1;

    // Move score text when the window is resized
    let score = engine.texts.get_mut("score").unwrap();
    score.translation.x = engine.window_dimensions.x / 2.0 - 80.0;
    score.translation.y = engine.window_dimensions.y / 2.0 - 30.0;

    let high_score = engine.texts.get_mut("high_score").unwrap();
    high_score.translation.x = -engine.window_dimensions.x / 2.0 + 100.0;
    high_score.translation.y = engine.window_dimensions.y / 2.0 - 30.0;

    // Handles collisions of the player car
    for event in engine.collision_events.drain(..) {
        debug!("{} is in collision with {}", event.pair.0, event.pair.1);
        let player_col = event.pair.one_starts_with("player");
        let barrel_col = event.pair.0.contains("barrel") || event.pair.1.contains("barrel");
        let car_col = event.pair.0.contains("car") || event.pair.1.contains("car");
        if event.state == CollisionState::Begin {
            if player_col && barrel_col {
                // When the player hits a barrel they score 1 point and the barrel disappears
                info!("Player hit a barrel");
                for label in [event.pair.0, event.pair.1] {
                    if label.contains("barrel") {
                        engine.sprites.remove(&label);
                    }
                }
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
            } else if player_col && car_col {
                // When the player hits another car the game is over, resetting the score and position
                info!("Game Over!");
                engine.audio_manager.play_sfx(SfxPreset::Jingle3, 0.5);
                let player = engine.sprites.get_mut("player").unwrap();
                player.translation = Vec2::new(0.0, 0.0);
                player.rotation = RIGHT;
                game_state.current_score = 0;
                let score = engine.texts.get_mut("score").unwrap();
                score.value = format!("Score: {}", game_state.current_score);
                game_state.movement_speed = 100.0;
            } else {
                // When a barrel is in a colision with another NPC sprite it is moved
                debug!("Two NPC sprites collided");
                let x_range = engine.window_dimensions.x.clone() / 2.0 - 50.0;
                let y_range = engine.window_dimensions.y / 2.0 - 50.0;
                let label: String;
                if event.pair.0.contains("barrel") {
                    // Move the barrel not the car, if there are 2 barrels the fist is moved
                    label = event.pair.0.clone();
                } else {
                    label = event.pair.1.clone();
                }
                let barrel_opt = engine.sprites.get_mut(&label);
                if barrel_opt.is_some() {
                    debug!("The sprite {} was moved", label);
                    let barrel = barrel_opt.unwrap();
                    barrel.translation.x = thread_rng().gen_range(-x_range..x_range);
                    barrel.translation.y = thread_rng().gen_range(-y_range..y_range);
                } else {
                    warn!(target: "game_logic::collision_events", "Error could not move barrel when {} is in collision with {}", event.pair.0, event.pair.1);
                }
                break;
            }
        }
    }

    // Move the car to the other side of the window when it hits the edge
    let player = engine.sprites.get_mut("player").unwrap();

    if player.translation.x > engine.window_dimensions.x / 2.0 - 1.0 {
        player.translation.x = -engine.window_dimensions.x / 2.0 + 10.0;
        debug!(
            "The car moved off the screen, moved to x = {}",
            player.translation.x
        );
    } else if player.translation.x < -engine.window_dimensions.x / 2.0 + 1.0 {
        player.translation.x = engine.window_dimensions.x / 2.0 - 10.0;
        debug!(
            "The car moved off the screen, moved to x = {}",
            player.translation.x
        );
    }
    if player.translation.y > engine.window_dimensions.y / 2.0 - 1.0 {
        // player.translation.y = -engine.window_dimensions.y / 2.0 + 10.0;
        player.translation.y = -350.0;
        debug!(
            "The car moved off the top of the screen, moved to y = {}",
            player.translation.y
        );
    } else if player.translation.y < -engine.window_dimensions.y / 2.0 + 1.0 {
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

    // Handles keyboard movement
    if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Up, KeyCode::W])
    {
        player.rotation = UP;
        player.translation.y += game_state.movement_speed * engine.delta_f32;
        if player.translation.y > engine.window_dimensions.y / 2.0 {
            player.translation.y = -engine.window_dimensions.y;
        }
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Down, KeyCode::S])
    {
        player.rotation = DOWN;
        player.translation.y -= game_state.movement_speed * engine.delta_f32;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Left, KeyCode::A])
    {
        player.rotation = LEFT;
        player.translation.x -= game_state.movement_speed * engine.delta_f32;
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Right, KeyCode::D])
    {
        player.rotation = RIGHT;
        player.translation.x += game_state.movement_speed * engine.delta_f32;
    }

    // Creates a barrel after Timer has run and sets it to a random position on the screen
    // a maximum number of barrels are created and then exisiting ones are moved
    if game_state.spawn_timer.tick(engine.delta).just_finished() {
        engine.audio_manager.play_sfx(SfxPreset::Click, 1.0);
        let x_range = engine.window_dimensions.x / 2.0 - 50.0;
        let y_range = engine.window_dimensions.y / 2.0 - 50.0;
        if game_state.barrel_index > game_state.max_barrels {
            game_state.barrel_index = 0;
        }
        game_state.barrel_index += 1;
        let label = format!("barrel{}", game_state.barrel_index);
        let barrel = engine.add_sprite(label.clone(), SpritePreset::RacingBarrelRed);
        barrel.translation.x = thread_rng().gen_range(-x_range..x_range);
        //barrel.translation.y = thread_rng().gen_range(-y_range..y_range);
        barrel.collision = true;
    }

    // NPC cars move each tick of the move_timer
    // if game_state.move_timer.tick(engine.delta).just_finished() {
    //     for i in 0..game_state.number_cars {
    //         let label = format!("car{}", i);
    //         let car_opt = engine.sprites.get_mut(&label);
    //         if car_opt.is_some() {
    //             let car = car_opt.unwrap();
    //             let x_range = engine.window_dimensions.x / 2.0 - 50.0;
    //             let y_range = engine.window_dimensions.y / 2.0 - 50.0;
    //             let x_move = thread_rng().gen_range(-10..10) as f32;
    //             let y_move = thread_rng().gen_range(-10..10) as f32;
    //             if (car.translation.x + x_move).abs() < x_range {
    //                 car.translation.x += x_move;
    //             } else {
    //                 car.translation.x -= x_move;
    //             }
    //             if (car.translation.y + y_move).abs() < y_range {
    //                 car.translation.y += y_move;
    //             } else {
    //                 car.translation.y -= y_move;
    //             }
    //         } else {
    //             warn!(target: "game_logic::move", "Error could not move NPC car {}", label);
    //         }
    //     }
    // }
}

fn main() {
    let mut game = Game::new();

    // Set up of initial sprites and scoreboard
    let player = game.add_sprite("player", SpritePreset::RacingCarBlue);
    player.translation = Vec2::new(10.0, 10.0);
    player.rotation = RIGHT;
    player.collision = true;

    for i in 0..2 {
        // Creates 4 cars, one in each corner
        let label = format!("car{}", i);
        let car = game.add_sprite(label, SpritePreset::RacingCarYellow);
        let x_pos: i32 = (i / 2 * 2 - 1) * 300; // sets the positions to + and - 300
        let y_pos: i32 = (i % 2 * 2 - 1) * 0; // sets the positions to + and - 150
        car.translation = Vec2::new(x_pos as f32, y_pos as f32);
        car.collision = true;
    }

    let score = game.add_text("score", "Score: 0");
    score.translation = Vec2::new(-520.0, 320.0);

    let high_score = game.add_text("high_score", "High Score: 0");
    high_score.translation = Vec2::new(520.0, 320.0);

    // Play music and run the game
    game.audio_manager
        .play_music(MusicPreset::WhimsicalPopsicle, 0.1);
    game.add_logic(game_logic);
    game.run(GameState::default());
}
