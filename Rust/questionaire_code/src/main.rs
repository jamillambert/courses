fn partition(seq: Vec<i32>, pred: &str) -> (Vec<i32>, Vec<i32>) {
    // Returns a vector of ints, the first pred is false and second it is true
    let mut is_true = Vec::new();
    let mut is_false = Vec::new();
    for n in seq {
        if pred_check(pred, n) {
            is_true.push(n);
        } else {
            is_false.push(n);
        }
    }
    return (is_false, is_true);
}

fn pred_check(pred: &str, n: i32) -> bool {
    // Returns true if pred is true for the input number
    // if pred is not recognised false is returned
    if pred == "is_odd" {
        return n % 2 != 0;
    } else if pred == "is_even" {
        return n % 2 == 0;
    } else if pred == "is_negative" {
        return n < 0;
    } else if pred == "is_positive" {
        return n >= 0;
    } else {
        return false;
    }
}

fn chunkify(s: &str, n: u32, fill: Option<char>) -> Vec<String> {
    // Returns a vector where each element is the input string split
    // into the specified length.  The last element is filled to the
    // specified length with the fill character, or 'x' if None is input
    let f = fill.unwrap_or('x');
    let mut chunks = Vec::new();
    let mut chunk = String::from("");
    let mut i = 0;
    for c in s.chars() {
        if i == n {
            // chunk is at length n, add to vector
            chunks.push(chunk);
            chunk = String::from("");
            i = 0;
        }
        chunk.push(c);
        i += 1;
    }
    while chunk.chars().count() as u32 % n != 0 {
        // fill up to length n with fill char f
        chunk.push(f);
    }
    chunks.push(chunk);
    return chunks;
}

fn strlen(s: &str) -> u32 {
    // Returns the number of graphemes in the input string
    let mut count = 0;
    let mut extra_bytes = 0;
    for c in s.as_bytes() {
        println!("{}", c);
        if c >> 5 == 0b110 {
            // char is 2 bytes long, should only count as 1 char
            extra_bytes += 1;
        } else if c >> 4 == 0b1110 {
            // char is 3 bytes long, should only count as 1 char
            extra_bytes += 2;
        } else if c >> 3 == 0b11110 {
            // char is 4 bytes long, should only count as 1 char
            extra_bytes += 3;
        }
        count += 1;
    }
    count - extra_bytes
}

fn atoi(s: &str) -> i32 {
    // Returns a single integer from the input string.
    // non numerical characters are ignored and
    // 0 is returned if the string contains no numbers
    let mut number = 0;
    let mut sign = 1;
    for c in s.chars() {
        if c == '-' {
            sign = -1;
        }
        else if 0 <= c as i32 - 0x30 && c as i32 - 0x30 <= 9 {
            number = number * 10 + c as i32 - 0x30;
        }
    }
    sign * number
}

fn main() {
    let string = "a";
    let number = atoi(string);
    println!("{}", number);
    let string2 = "😂";
    println!(
        "byte length is {}, char length is {}, grapheme length is {}",
        string2.len(),
        string2.chars().count(),
        strlen(string2)
    );
    let string = "12345678910";
    println!("chunkify {:?}", chunkify(string, 2, Some('r')));
    let vector = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let (is_false, is_true) = partition(vector, "is_even");
    println!("partition false: {:?}, true {:?}", is_false, is_true);
    let one = 240;
    println!("one {}, shifted 3 {}, shifted 4 {} shifted 5 {}", one, one >> 3, one >> 4, one >> 5);
}
