use hello::greet;
use rand::thread_rng;
use rand::Rng;

fn main() {
    greet();
    let x = thread_rng().gen_range(0, 100);
    println!("{}", x)
}
