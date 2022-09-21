fn main() {
let mut string = String::from("initial"); 
foo(&mut string);
println!("{}", string);
}

fn foo(string: &mut String) {
    *string += " x";
    barr(string);
}

fn barr(string: &mut String) {
    *string += " x";
}