#[no_mangle]
pub extern fn simple_add(a: i32, b: i32) -> i32 { a + b}


#[no_mangle]
pub extern fn fibo(n: i32) -> i32 {
    if n < 0 {
        panic!("{} is negative!", n);
    } else if n == 0 {
        panic!("zero is not a right argument to fibonacci()!");
    } else if n == 1 {
        return 1;
    }

    let mut sum = 0;
    let mut last = 0;
    let mut curr = 1;
    for _i in 1..n {
        sum = last + curr;
        last = curr;
        curr = sum;
    }
    sum
}

#[no_mangle]
pub extern fn loop_str(string: String) -> () {
    // for strings types in Rust see http://www.suspectsemantics.com/blog/2016/03/27/string-types-in-rust/
    for c in string.chars() {
        let _s = c.to_digit(10).unwrap() * 10;
    }
}
