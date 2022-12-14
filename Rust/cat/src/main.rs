use std::env;
use std::fs;

fn cat(file: &String, options: &Vec<char>) {
    // Outputs the file to the terminal formatted with options
    let contents = fs::read(file).unwrap();
    let text = String::from_utf8_lossy(&contents);
    let mut line_no = 0;
    let mut non_blank_lines = 0;
    let mut previous_blank = false;
    for line in text.lines() {
        line_no += 1;
        if options.contains(&'s') {
            if line.len() == 0 && previous_blank {
                continue;
            } else if line.len() == 0 {
                previous_blank = true;
            } else if previous_blank {
                previous_blank = false;
            }
        }
        if options.contains(&'b') {
            if line.len() != 0 {
                non_blank_lines +=1;
                print!("\x1b[42m{:>3} \x1b[0m", non_blank_lines);
            }
        }
        else if options.contains(&'n') {
            print!("\x1b[42m{:>3} \x1b[0m", line_no);
        }
        println!("{}", line);
    }
}

fn read_options(arg: &String) -> Vec<char> {
    // Returns a vector of characters of all implemented options in the input string
    let mut options = Vec::new();
    let implemented_options = ['n', 's', 'h', 'b'];
    for char in arg.chars() {
        if implemented_options.contains(&char) {
            options.push(char);
        }
    }
    return options;
}

fn print_help() {
    // Prints the help text
    println!("CAT written in Rust\n");
    println!("\x1b[1mNAME\x1b[0m");
    println!("\tcat - concatenate files and print on the standard output\n");
    println!("\x1b[1mSYNOPSIS\x1b[0m");
    println!("\tcat [OPTION]... [FILE]...\n");
    println!("\x1b[1mDESCRIPTION\x1b[0m");
    println!("\t-h\tdisplay this help and exit\n");
    println!("\t-n\tnumber all output lines\n");
    println!("\t-b\tnumber nonempty output lines, overrides -n\n");
    println!("\t-s\tsuppress repeated empty output lines\n");
    println!("\x1b[1mEXAMPLES\x1b[0m");
    println!("\tcat -ns file1.txt file2.txt");
    println!("\t\toutput file1.txt and then file2.txt contents with line numbering and");
    println!("\t\trepeated empty lines suppressed.\n");
    println!("\x1b[1mAUTHOR\x1b[0m");
    println!("\tWritten by Jamil Lambert\n");
}
fn main() {
    // Reads in the options, if -h is used the help is printed and the program exits
    // otherwise each file in the list is passed to cat() to be output
    let args: Vec<String> = env::args().collect();
    let mut options = Vec::new();
    let mut start = 1;
    if args[1].chars().next().unwrap() == '-' {
        options = read_options(&args[1]);
        start = 2;
    }
    if options.contains(&'h') {
        print_help();
    } else {
        for i in start..args.len() {
            println!("arg: {}", args[i]);
            cat(&args[i], &options);
        }
    }
}
