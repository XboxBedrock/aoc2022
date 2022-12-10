use std::io;

fn main()  -> io::Result<()> {

    let mut user_input = String::new();
    let stdin = io::stdin();

    let mut iters = 0;

    stdin.read_line(&mut user_input).expect("STDIN failure");

    for (i, _c) in user_input.chars().enumerate() {
        let mut chars = String::new();

        for j in i..i+4 {
            if chars.contains(user_input.as_str().chars().nth(j).unwrap()) {
                break;
            }
            chars.push(user_input.as_str().chars().nth(j).unwrap());
        }

        if chars.chars().count() == 4 { break; }
        
        iters+=1;
    }

    println!("{}", iters+4);

    Ok(())
}
