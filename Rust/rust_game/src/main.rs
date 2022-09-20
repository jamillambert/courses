use rusty_engine::prelude::{bevy::prelude::default, *};

struct GameState {
    name: String,
    health_left: i32,
    high_score: i32,
    current_score: i32,
    enemy_labels: Vec<String>,
    spawn_timer: Timer,
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
        }
    }
}

fn main() {
    let mut game = Game::new();
    game.run(GameState::default());
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {
    game_state.current_score += 1;
    println!("Current score: {}", game_state.current_score);
}
