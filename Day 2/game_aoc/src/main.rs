use std::fs::File;
use std::io::{BufReader, BufRead};
use std::str;
use regex::Regex;

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);
    //let red_max = 12;
    //let green_max = 13;
    //let blue_max = 14;

    //let mut running_game_sum = 0;
    let mut running_power_sum = 0;

    for line in reader.lines() {
        //let mut is_game_valid = true;
        let line = line?;
        let split_on_colon = line.split(":").collect::<Vec<&str>>(); 
        //here we have game number on one side, and games on the other
        
        //find game number
        let game_str = split_on_colon[0];
        let game_number = find_game_number(&game_str);
        
        println!("Game Number: {}", game_number);

        //split second part on semi colons into rounds of game
        let round_split = split_on_colon[1].split(";").collect::<Vec<&str>>();
        //println!("{:?}", round_split);

        //split rounds by commas
        let mut red_min = 0;
        let mut green_min = 0;
        let mut blue_min = 0;
        for round in round_split {
            let color_and_amount_vec = round.split(",").collect::<Vec<&str>>();
            for color_and_amount in color_and_amount_vec{
                let (color, number) = find_color_and_number(&color_and_amount);
                match color{
                    _ if color == "red" =>{
                        if number > red_min {
                            red_min = number;
                        }
                    },
                    _ if color == "green" =>{
                        if number > green_min {
                            green_min = number;
                        }
                    },
                    _ if color == "blue" =>{
                        if number > blue_min {
                            blue_min = number;
                        }
                    },
                    _ => println!("nothing"),
                }
            }
        }
        let power = red_min * green_min * blue_min;
        //println!("Red Min: {}\nGreen Min: {}\nBlue Min: {}\nPower: {}",red_min, green_min, blue_min, power)
        /*if is_game_valid{
            running_game_sum += game_number;
        } */
        running_power_sum += power;
    }
    //println!("Game Sum: {}", running_game_sum);
    println!("Power Sum: {}", running_power_sum);
    Ok(())
}

fn find_game_number(x: &str) -> i32{
    let number = &x[5..];
    //println!("Game Number: {}", number)
    return number.parse::<i32>().unwrap();
}

fn find_color_and_number(x: &str) -> (String, i32) {
    let input = x.to_string();
    let number_match = Regex::new(r"[0-9 ]").unwrap();
    let color = number_match.replace_all(&input, "");

    let letter_match = Regex::new(r"[A-Za-z ]").unwrap();
    let number = letter_match.replace_all(&input, "");
    //println!("Color: {}, Number: {}", color, number);
    return (color.to_string(), number.parse::<i32>().unwrap());
}