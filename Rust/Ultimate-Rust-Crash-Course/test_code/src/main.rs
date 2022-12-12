fn strlen(s: String) -> u32{
    // Returns the number of graphemes in the input string
    let mut count = 0;
    for c in s.as_bytes(){
        if c >> 5 == 0b110 {
            // char is 2 bytes long, should only count as 1 char
            count -= 1;
        }
        else if c >> 4 == 0b1110 {
            // char is 3 bytes long, should only count as 1 char
            count -= 2;
        }
        else if c >> 3 == 0b11110 {
            // char is 4 bytes long, should only count as 1 char
            count -= 3;
        }
        count += 1;
    }
    return count;
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

fn main() {
    let string = String::from("12s3a"); 
    let number = atoi(string);
    println!("{}", number);
    let string2 = String::from("12é3a😃"); 
    println!("byte length is {}, char length is {}, grapheme length is {}", string2.len(), string2.chars().count(), strlen(string2));
}
