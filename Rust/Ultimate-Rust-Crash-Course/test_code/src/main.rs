
fn main() {
        let args: Vec<String> = std::env::args().skip(1).collect();
        for fruit in args {
            match fruit.as_str() {
                "apple" => {
                    println!("Fruit {} is an apple", fruit);
                }
                "pear" => {
                    println!("Fruit {} is a pear", fruit);
                }
                _ => {
                    println!("Fruit {} is not an apple or a pear", fruit);
                }
            }
        }
    }
