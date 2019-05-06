#[no_mangle]
pub extern fn simple_add(a: i32, b: i32) -> i32 { a + b}

///
/// Fibonacci
/// https://github.com/eliovir/rust-examples/blob/master/fibonacci.rs
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

use geo::{Polygon, LineString};
use geo::convexhull::ConvexHull;
///
/// Constructive operations: Convex hull in Rust Geo
///
#[no_mangle]
pub extern fn rust_geo_convex_hull() -> () {
    // An L shape
    let coords = vec![
        (0.0, 0.0),
        (4.0, 0.0),
        (4.0, 1.0),
        (1.0, 1.0),
        (1.0, 4.0),
        (0.0, 4.0),
        (0.0, 0.0)];
    // conversions to geo types are provided from several kinds of coordinate sequences
    let poly = Polygon::new(coords.into(), vec![]);

    // uses the QuickHull algorithm to calculate the polygon's convex hull
    let hull = poly.convex_hull();

}
