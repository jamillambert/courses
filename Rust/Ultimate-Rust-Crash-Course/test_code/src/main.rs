
fn main() {
    let x = String::from("test string");
    println!("main {}", x);
    print_test(&x);
    println!("after test {}", x);
}

fn print_test(s: &String) {
    println!("test {}", s);
}
