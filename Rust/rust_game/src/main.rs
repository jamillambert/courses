use rusty_engine::{prelude::{bevy::prelude::default, *}, game};
use std::time::SystemTime;

struct GameState {
    name: String,
    health_left: i32,
    high_score: i32,
    current_score: i32,
    enemy_labels: Vec<String>,
    spawn_timer: Timer,
    measure_time: SystemTime,
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
            measure_time: SystemTime::now(),
        }
    }
}

fn main() {
    let mut game = Game::new();
    game.add_logic(game_logic);
    game.run(GameState::default());
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {
    if game_state.current_score % 60 == 0 {
       let new_time = SystemTime::now();
        let fps = 60000 / SystemTime::duration_since(&new_time, game_state.measure_time).unwrap().as_millis();
        game_state.measure_time = new_time;
        println!("Current score: {}, fps: {}", game_state.current_score, fps);
    }
    game_state.current_score += 1;
}
