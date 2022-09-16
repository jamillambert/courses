use rusty_engine::prelude::*;

struct GameState {
    name: String,
    health_left: i32,
    high_score: i32,
    current_score: i32,
    enemy_labels: Vec<String>,
    spawn_timer: Timer,
}

impl Default for GameState {
}

fn main() {
    let mut game = Game::new();

    // get your game stuff ready here

    game.run(GameState { health_left: 42 });
}