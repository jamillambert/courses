
fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    print_vec(& args);
}

fn print_vec(args: &Vec<String>) {
    for arg in args {
        println!("{}", arg);
    }
}
