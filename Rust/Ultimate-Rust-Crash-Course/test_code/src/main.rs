
fn main() {
        let args: Vec<String> = std::env::args().skip(1).collect();
        for fruit in args {
            let message = match fruit.as_str() {
                "apple" => {
                    format!("Fruit {} is an apple", fruit)
                }
                "pear" => {
                    format!("Fruit {} is a pear", fruit)
                }
                _ => {
                    format!("Fruit {} is not an apple or a pear", fruit)
                }
            };
            println!("{}", message);
        }
    }
