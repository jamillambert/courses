use rusty_engine::{
    game,
    prelude::{bevy::prelude::default, *},
};
use std::{time::SystemTime, f32::consts::PI};

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
    movement_direction: f32,
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
            movement_direction: 0.0,
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

    // Handles collisions with the player
    for event in engine.collision_events.drain(..) {
        if event.state == CollisionState::Begin && event.pair.one_starts_with("player") {
            for label in [event.pair.0, event.pair.1] {
                if label != "player" {
                    engine.sprites.remove(&label);
                }
            } 
            game_state.movement_direction += PI;
        }
    }

    // Handles keyboard movement
    let player = engine.sprites.get_mut("player").unwrap();
    if engine.keyboard_state.pressed(KeyCode::Up) {
        player.rotation = UP;
        player.translation.y += game_state.movement_speed * engine.delta_f32;
    } else if engine.keyboard_state.pressed(KeyCode::Down) {
        player.rotation =  DOWN;
        player.translation.y -= game_state.movement_speed * engine.delta_f32;
    } else if engine.keyboard_state.pressed(KeyCode::Left) {
        player.rotation = LEFT;
        player.translation.x -= game_state.movement_speed * engine.delta_f32;
    } else if engine.keyboard_state.pressed(KeyCode::Right) {
        player.rotation = RIGHT;
        player.translation.x += game_state.movement_speed * engine.delta_f32;
    }
}

fn main() {
    let mut game = Game::new();
    let player = game.add_sprite("player", SpritePreset::RacingCarBlue);
    player.translation = Vec2::new(10.0, 10.0);
    player.rotation = RIGHT;
    player.collision = true;
    // let player::speed = 100;

    let car1 = game.add_sprite("car1", SpritePreset::RacingCarYellow);
    car1.translation = Vec2::new(300.0, 0.0);
    car1.collision = true;

    game.add_logic(game_logic);
    game.run(GameState::default());
}
