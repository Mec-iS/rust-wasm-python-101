extern crate geo;
extern crate rustc_version_runtime;

use std::fs;
use rustc_version_runtime::version;
///
/// Write Rust version and cfg in a file
///
pub extern fn startup() -> () {
    let version: String = version().to_string();
    let data = format!("rustc: {:?}\n", version);
    fs::write("./CONFIG", data).expect("Unable to write file");

}

fn main() {
    println!("Writing CONFIG file");
    startup();
}
