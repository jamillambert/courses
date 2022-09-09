// FINAL PROJECT
//
// Create an image processing application.  Exactly what it does and how it does
// it is up to you, though I've stubbed a good amount of suggestions for you.
// Look for comments labeled **OPTION** below.
//
// Two image files are included in the project root for your convenience: dyson.png and pens.png
// Feel free to use them or provide (or generate) your own images.
//
// Don't forget to have fun and play around with the code!
//
// Documentation for the image library is here: https://docs.rs/image/0.21.0/image/
//
// NOTE 1: Image processing is very CPU-intensive.  Your program will run *noticeably* faster if you
// run it with the `--release` flag.
//
//     cargo run --release [ARG1 [ARG2]]
//
// For example:
//
//     cargo run --release blur image.png blurred.png
//
// NOTE 2: This is how you parse a number from a string (or crash with a
// message). It works with any integer or float type.
//
//     let positive_number: u32 = some_string.parse().expect("Failed to parse a number");

fn main() {
    // 1. First, you need to implement some basic command-line argument handling
    // so you can make your program do different things.  Here's a little bit
    // to get you started doing manual parsing.
    //
    // Challenge: If you're feeling really ambitious, you could delete this code
    // and use the "clap" library instead: https://docs.rs/clap/2.32.0/clap/
    let mut args: Vec<String> = std::env::args().skip(1).collect();
    if args.len() < 2 {
        print_usage_and_exit();
    }
    let infile = args.remove(0);
    let mut img = image::open(infile).expect("Failed to open INFILE.");
    let outfile = args.remove(0);
    // if outfile.as_str() == "fractal" {
    //     fractal(infile);
    // }
    while args.len() > 0 {
        let subcommand = args.remove(0);
        match subcommand.as_str() {
            "blur" => {
                if args.len() < 1 {
                    print_usage_and_exit();
                }
                let amount: f32 = args.remove(0).parse().unwrap();
                img = blur(img, amount);
            }
            "brighten" => {
                if args.len() < 1 {
                    print_usage_and_exit();
                }
                let amount: i32 = args.remove(0).parse().unwrap();
                img = brighten(img, amount);
            }
            "crop" => {
                if args.len() < 4 {
                    print_usage_and_exit();
                }
                let x: u32 = args.remove(0).parse().unwrap();
                let y: u32 = args.remove(0).parse().unwrap();
                let width: u32 = args.remove(0).parse().unwrap();
                let height: u32 = args.remove(0).parse().unwrap();
                img = crop(img, x, y, width, height);
            }
            "rotate" => {
                if args.len() < 1 {
                    print_usage_and_exit();
                }
                let angle: u32 = args.remove(0).parse().unwrap();
                img = rotate(img, angle);
            }
            "invert" => {
                img = invert(img);
            }
            "grayscale" => {
                img = grayscale(img);
            }
            "fractal" => {
                img = fractal();
            }
            _ => {
                print_usage_and_exit();
            }
        }
    }
    img.save(outfile).expect("Failed writing OUTFILE.");
}

fn print_usage_and_exit() {
    println!("USAGE (when in doubt, use a .png extension on your filenames)");
    println!("INFILE OUTFILE (command options) (command2 options2) ...");
    println!("Where (command options) are in the following list:");
    println!("brighten amount<i32>");
    println!("crop x<u32> y<u32> width<u32> height<u32>");
    println!("rotate amount<90, 180 or 270>");
    println!("invert");
    println!("grayscale");
    println!("fractal");
    println!("e.g. image1.png image1_modified.png rotate 90");
    println!("or e.g. image1.png fractal");
    std::process::exit(-1);
}

fn blur(img: image::DynamicImage, amount: f32) -> image::DynamicImage {
    img.blur(amount)
}

fn brighten(img: image::DynamicImage, amount: i32) -> image::DynamicImage {
    img.brighten(amount) // positive numbers brighten the image. Negative numbers darken it
}

fn crop(
    mut img: image::DynamicImage,
    x: u32,
    y: u32,
    width: u32,
    height: u32,
) -> image::DynamicImage {
    img.crop(x, y, width, height)
}

fn rotate(img: image::DynamicImage, angle: u32) -> image::DynamicImage {
    match angle {
        90 => img.rotate90(),
        180 => img.rotate180(),
        270 => img.rotate270(),
        _ => img,
    }
}

fn invert(mut img: image::DynamicImage) -> image::DynamicImage {
    img.invert();
    return img;
}

fn grayscale(img: image::DynamicImage) -> image::DynamicImage {
    img.grayscale()
}

// This code was adapted from https://github.com/PistonDevelopers/image
fn fractal() -> image::DynamicImage {
    let width = 800;
    let height = 800;

    let mut imgbuf = image::ImageBuffer::new(width, height);

    let scale_x = 3.0 / width as f32;
    let scale_y = 3.0 / height as f32;

    // Iterate over the coordinates and pixels of the image
    for (x, y, pixel) in imgbuf.enumerate_pixels_mut() {
        // Use red and blue to be a pretty gradient background
        let red = (0.3 * x as f32) as u8;
        let blue = (0.3 * y as f32) as u8;

        // Use green as the fractal foreground (here is the fractal math part)
        let cx = y as f32 * scale_x - 1.5;
        let cy = x as f32 * scale_y - 1.5;

        let c = num_complex::Complex::new(-0.4, 0.6);
        let mut z = num_complex::Complex::new(cx, cy);

        let mut green = 0;
        while green < 255 && z.norm() <= 2.0 {
            z = z * z + c;
            green += 1;
        }

        // Actually set the pixel. red, green, and blue are u8 values!
        *pixel = image::Rgb([red, green, blue]);
    }

    return image::ImageRgb8(imgbuf);
}

// **SUPER CHALLENGE FOR LATER** - Let's face it, you don't have time for this during class.
//
// Make all of the subcommands stackable!
//
// For example, if you run:
//
//   cargo run infile.png outfile.png blur 2.5 invert rotate 180 brighten 10
//
// ...then your program would:
// - read infile.png
// - apply a blur of 2.5
// - invert the colors
// - rotate the image 180 degrees clockwise
// - brighten the image by 10
// - and write the result to outfile.png
//
// Good luck!
