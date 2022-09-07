
fn main() {
    let mut x = String::from("test string");
    println!("main {}", x);
    print_test(&mut x);
    println!("after test {}", x);
}

fn print_test(s: &mut String) {
    println!("test {}", s);
    *s = String::from("Run once");
}
