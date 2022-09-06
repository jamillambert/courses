const STARTING_MISSILES: i32 = 8;
const READY_AMMOUNT: i32 = 2;
fn main() {
    let mut missiles = STARTING_MISSILES;
    let ready = READY_AMMOUNT;
    println!("Firing {} of my {} missiles...", ready, missiles);
    missiles -= ready;
    println!("{} missiles left", missiles);
}
