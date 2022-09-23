#![allow(unused_variables, unused_attributes, dead_code, unused_imports)] //to remove warnings bofore the code is done
use log::{debug, info};
use rand::prelude::*;
use rusty_engine::prelude::*;
use std::{f32::consts::PI, time::SystemTime};

struct GameState {
    health_amount: u8,
    lost: bool,
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
            health_amount: 100,
            lost: false,
            high_score: 10,
            current_score: 0,
            frame_no: 0,
            measure_time: SystemTime::now(),
            movement_speed: 100.0,
            barrel_index: 0,
            spawn_timer: Timer::from_seconds(1.0, true),
            max_barrels: 4,
            window_x: 0.0,
            window_y: 0.0,
        }
    }
}

fn reset_game(engine: &mut Engine, game_state: &mut GameState) {
    engine.sprites.clear();
    let player = engine.add_sprite("player", SpritePreset::RacingCarBlue);
    player.translation = Vec2::new(0.0, -500.0); 
    player.layer = 50.0;
    player.rotation = RIGHT;
    player.collision = true;
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {    
    if game_state.frame_no == 0 {
        reset_game(engine, game_state);
    }
    game_state.frame_no += 1;    
    if game_state.window_x != engine.window_dimensions.x
        || game_state.window_y != engine.window_dimensions.y
    {
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
}

fn main() {
    let mut game = Game::new();
    let game_state = GameState::default();

    let score = game.add_text("score", "Score: 0");
    score.translation = Vec2::new(-520.0, 320.0);

    let high_score = game.add_text("high_score", format!("High Score: {}", game_state.high_score));
    high_score.translation = Vec2::new(520.0, 320.0);

    // Play music and run the game
    game.audio_manager
        .play_music(MusicPreset::WhimsicalPopsicle, 0.1);
    game.add_logic(game_logic);
    game.run(game_state);
}