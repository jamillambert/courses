use rusty_engine::{
    game,
    prelude::{bevy::prelude::default, *},
};
use std::time::SystemTime;

struct GameState {
    name: String,
    health_left: i32,
    high_score: i32,
    current_score: i32,
    enemy_labels: Vec<String>,
    spawn_timer: Timer,
    frame_no: u32,
    measure_time: SystemTime,

    movement_speed: f32,
    barrel_index: i32, // index for spawned barrels any time the mouse is clicked
}

impl Default for GameState {
    fn default() -> Self {
        Self {
            name: "Player".to_string(),
            health_left: 0,
            high_score: 0,
            current_score: 0,
            enemy_labels: Vec::new(),
            spawn_timer: Timer::from_seconds(1.0, false),
            frame_no: 0,
            measure_time: SystemTime::now(),

            movement_speed: 100.0,
            barrel_index: 0,
        }
    }
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {
    // Show current fps
    if game_state.frame_no % 100 == 0 {
        let new_time = SystemTime::now();
        let fps = 100000
            / SystemTime::duration_since(&new_time, game_state.measure_time)
                .unwrap()
                .as_millis();
        game_state.measure_time = new_time;
        println!("Current score: {}, fps: {}", game_state.current_score, fps);
    }
    game_state.frame_no += 1;
    // Handles collisions of the player car
    for event in engine.collision_events.drain(..) {
        if event.state == CollisionState::Begin
            && event.pair.one_starts_with("player")
            && event.pair.one_starts_with("barrel")
        {  // When the player hits a barrel they score 1 point and the barrel disappears
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
                game_state.high_score = game_state.current_score;
                let high_score = engine.texts.get_mut("high_score").unwrap();
                high_score.value = format!("High Score: {}", game_state.high_score);
            }
        } else if event.state == CollisionState::Begin
            && event.pair.one_starts_with("player")
            && event.pair.one_starts_with("car")
        { // When the player hits another car the game is over, resetting the score and position
            let player = engine.sprites.get_mut("player").unwrap();
            player.translation = Vec2::new(0.0, 0.0);
            player.rotation = RIGHT;
            game_state.current_score = 0;
            let score = engine.texts.get_mut("score").unwrap();
            score.value = format!("Score: {}", game_state.current_score);
            game_state.movement_speed = 100.0;
        }
    }

    let player = engine.sprites.get_mut("player").unwrap();

    // Handles keyboard movement
    if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Up, KeyCode::W])
    {
        player.rotation = UP;
        player.translation.y += game_state.movement_speed * engine.delta_f32;
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

    // Creates a barrel sprite at the mouse location when the left button is clicked
    if engine.mouse_state.just_pressed(MouseButton::Left) {
        if let Some(mouse_location) = engine.mouse_state.location() {
            let label = format!("barrel{}", game_state.barrel_index);
            game_state.barrel_index += 1;
            let barrel = engine.add_sprite(label.clone(), SpritePreset::RacingBarrelRed);
            barrel.translation = mouse_location;
            barrel.collision = true;
        }
    }
}

fn main() {
    let mut game = Game::new();
    let player = game.add_sprite("player", SpritePreset::RacingCarBlue);
    player.translation = Vec2::new(10.0, 10.0);
    player.rotation = RIGHT;
    player.collision = true;

    let score = game.add_text("score", "Score: 0");
    score.translation = Vec2::new(-520.0, 320.0);

    let high_score = game.add_text("high_score", "High Score: 0");
    high_score.translation = Vec2::new(520.0, 320.0);

    let car1 = game.add_sprite("car1", SpritePreset::RacingCarYellow);
    car1.translation = Vec2::new(300.0, 150.0);
    car1.collision = true;      
    let car1 = game.add_sprite("car2", SpritePreset::RacingCarRed);
    car1.translation = Vec2::new(-300.0, -150.0);
    car1.collision = true;
    let car1 = game.add_sprite("car3", SpritePreset::RacingCarGreen);
    car1.translation = Vec2::new(300.0, 150.0);
    car1.collision = true;      
    let car1 = game.add_sprite("car4", SpritePreset::RacingCarBlack);
    car1.translation = Vec2::new(-300.0, -150.0);
    car1.collision = true;


    game.add_logic(game_logic);
    game.run(GameState::default());
}
