#![allow(unused_variables, unused_attributes, dead_code, unused_imports)] //to remove warnings bofore the code is done
use log::{debug, info};
use rand::prelude::*;
use rusty_engine::prelude::*;
use std::{f32::consts::PI, time::SystemTime};

const TURN_SPEED: f32 = 0.5;
const PLAYER_SPEED: f32 = 100.0;
const MAX_TURN: f32 = 10.0;
const MAX_SPEED: f32 = 700.0;

struct GameState {
    health_amount: u8,
    lost: bool,
    high_score: i32,
    current_score: i32,
    frame_no: u32,
    measure_time: SystemTime,
    movement_speed: f32,
    direction: f32,
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
            movement_speed: 50.0,
            direction: 0.0,
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
    let x = -game_state.window_x / 2.0 + 80.0;
    let y = 0.0;
    player.translation = Vec2::new(x, y); 
    player.layer = 50.0;
    player.rotation = RIGHT;
    player.collision = true;
     
    for i in 0..10 {
        let roadline = engine.add_sprite(format!("roadline{}", i), SpritePreset::RacingBarrierWhite);
        roadline.scale = 0.1;
        let line_x = game_state.window_x / 2.0 - game_state.window_x / 10.0 * i as f32;
        roadline.translation.x = line_x;
    }
}

fn loop_motion(sprite: &mut Sprite, game_state: &mut GameState) {
    if sprite.translation.x > game_state.window_x / 2.0 + 1.0 {
        sprite.translation.x = -game_state.window_x / 2.0;
        debug!(
            "The car moved off the screen, moved to x = {}",
            sprite.translation.x
        );
    } else if sprite.translation.x < -game_state.window_x / 2.0 - 1.0 {
        sprite.translation.x = game_state.window_x / 2.0;
        debug!(
            "The car moved off the screen, moved to x = {}",
            sprite.translation.x
        );
    }
    if sprite.translation.y > game_state.window_y / 2.0 {
        sprite.translation.y = -game_state.window_y / 2.0;
        debug!(
            "The car moved off the top of the screen, moved to y = {}",
            sprite.translation.y
        );
    } else if sprite.translation.y < -game_state.window_y / 2.0 {
        debug!(
            "The car moved off the screen, from y = {}",
            sprite.translation.y
        );
        sprite.translation.y = game_state.window_y / 2.0;
        debug!(
            "The car moved off the screen, moved to y = {}",
            sprite.translation.y
        );
    }
}

fn game_logic(engine: &mut Engine, game_state: &mut GameState) {    
    // if it is the first run of the game the reset_game function is run
    // to set up the in initial state of the game
    if game_state.frame_no == 0 {
        game_state.window_x = engine.window_dimensions.x;
        game_state.window_y = engine.window_dimensions.y;
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

        let score = engine.texts.get_mut("player").unwrap();
        score.translation.x = 0.0;
        score.translation.y = engine.window_dimensions.y / 2.0 - 30.0;
    }

    // Keyboard movement of the player
    if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Up, KeyCode::W])
    {
        if game_state.direction < MAX_TURN {
            game_state.direction += TURN_SPEED;
        }
        if game_state.movement_speed > 100.0 {
        game_state.movement_speed -= 5.0;
        }
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Down, KeyCode::S])
    {
        if game_state.direction > -MAX_TURN {
            game_state.direction -= TURN_SPEED;
        }
        if game_state.movement_speed > 100.0 {
        game_state.movement_speed -= 5.0;
        }
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Left, KeyCode::A])
    {
        if game_state.movement_speed > 0.0 {
        game_state.movement_speed -= 10.0;
        }
    } else if engine
        .keyboard_state
        .pressed_any(&[KeyCode::Right, KeyCode::D])
    {        
        if game_state.movement_speed < MAX_SPEED {
        game_state.movement_speed +=  10.0;
        }
    }
    let mut player = engine.sprites.get_mut("player").unwrap();
    player.rotation = game_state.direction * 0.1;
    player.translation.y += game_state.direction * engine.delta_f32 * game_state.movement_speed / MAX_TURN;
    loop_motion(&mut player, game_state);

    let player_text = engine.texts.get_mut("player").unwrap();
    player_text.value = format!("Player pos: {:.0}, {:.0} speed: {:.2} direction {:.2}", player.translation.x, player.translation.y, game_state.movement_speed, game_state.direction);

// Move the road lines to simulate motion of the car
    for mut sprite in engine.sprites.values_mut() {
        if sprite.label.starts_with("roadline"){
            sprite.translation.x -= game_state.movement_speed * engine.delta_f32;
            loop_motion(&mut sprite, game_state);
        }
    }

}

fn main() {
    let mut game = Game::new();
    let game_state = GameState::default();

    let score = game.add_text("score", "Score: 0");
    score.translation = Vec2::new(-520.0, 320.0);
    let high_score = game.add_text("high_score", format!("High Score: {}", game_state.high_score));
    high_score.translation = Vec2::new(520.0, 320.0);

    let score = game.add_text("player", "uninitialised");
    score.translation = Vec2::new(0.0, 320.0);


    // Play music and run the game
    game.audio_manager
        .play_music(MusicPreset::WhimsicalPopsicle, 0.1);
    game.add_logic(game_logic);
    game.run(game_state);
}