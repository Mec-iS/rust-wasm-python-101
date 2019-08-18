// Advantages on using:
// * std::os::raw::c_char;
// * std::ffi::CStr;
// * std::ffi::CString;
//
// 1. No need to define a type, everything is a Wasm reuntime's memory address
//    and can be referenced as such
//
// Advantages on using C bindings:
// 1. No explicit FFI, no headers, no linking; all safety advantages from Rust.
// 2. All functions accept a pointer and return a pointer.

#[no_mangle]
pub extern fn reverse_string(pointer: *mut u8, length: usize) -> *const u8 {
    let slice: &[u8] = unsafe { std::slice::from_raw_parts(pointer, length) };
    let string = std::str::from_utf8(slice).unwrap();
    let result = string.chars().rev().collect::<String>();
    result.into_bytes().as_ptr()
}
