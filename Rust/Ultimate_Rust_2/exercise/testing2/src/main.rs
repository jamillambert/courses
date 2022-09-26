pub fn fizz_buzz(x: i32, y: i32, z: i32) {
    let mut output = String::new();
    for i in 1..(z+1) {
        if i % x == 0 {
            output.push_str("Fizz");
        }
        if i % y == 0 {
            output.push_str("Buzz");
        }
        if i % x != 0 && i % y != 0 {
            output.push_str(&i.to_string());
        }
        output.push_str("\n");
    }
    println!("{}", output);
}

fn main() {
    fizz_buzz(3, 5, 100);
} 
