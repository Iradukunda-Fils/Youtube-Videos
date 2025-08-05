use std::env;

fn main(){
    println!("print something {}", 8);

//    let  string: &str = "hello, world";

    let age: i32 = 19;

    let valid = if age < 18 {"you are young"} else {"you are older"};

    let mut count: i32 =0;

    let _loop = loop{

        if count >= 3 {
            break count;
        }
        count += 1
    };


    println!("{}! {}", valid, _loop);
   
    println!("{:?}", env::args());

}