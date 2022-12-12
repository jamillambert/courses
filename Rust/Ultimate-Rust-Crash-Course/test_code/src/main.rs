fn main() {
    let string = String::from("12s3a"); 
    let number = atoi(string);
    println!("{}", number);
}

fn atoi(s: String) -> i32{
    // Returns an integer from the input string. 
    // non numerical characters are ignored and 
    // 0 is returned if the string contains no 
    let mut number = 0;
    for c in s.chars(){
        if 0 <= c as i32 - 0x30 && c as i32 - 0x30 <= 9 {
            number = number * 10 + c as i32 - 0x30;
        }
    }
    return number;
}

