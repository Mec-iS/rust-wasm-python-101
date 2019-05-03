#[no_mangle]
pub extern fn simple_add(a: i32, b: i32) -> i32 { a + b}

///
/// Fibonacci
///
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

///
/// Loop a string
///
#[no_mangle]
pub extern fn loop_str(string: String) -> () {
    // for strings types in Rust see http://www.suspectsemantics.com/blog/2016/03/27/string-types-in-rust/
    for c in string.chars() {
        let _s = c.to_digit(10).unwrap() * 10;
    }
}


///
/// Constructive operations: Convex hull in Rust Geo
///
#[no_mangle]
pub extern fn rust_geo_convex_hull() -> () {
    use geo::{line_string, polygon};
    use geo::convexhull::ConvexHull;

    // An L shape
    let poly = polygon![
       (x: 0.0, y: 0.0),
       (x: 4.0, y: 0.0),
       (x: 4.0, y: 1.0),
       (x: 1.0, y: 1.0),
       (x: 1.0, y: 4.0),
       (x: 0.0, y: 4.0),
       (x: 0.0, y: 0.0),
    ];

    // Ccalculate the polygon's convex hull
    poly.convex_hull();

}
