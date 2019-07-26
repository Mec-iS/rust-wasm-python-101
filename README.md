# rust-wasm-python-101

A basic example of calling Rust from Python used as example in the blogposts:
* [Rust-scales Python: Basic experiment](https://medium.com/@lorenzogotuned/rust-scales-python-function-d3b1d24351cd)
* [Rust-scales Python: Example 1](https://medium.com/@lorenzogotuned/rust-scales-python-some-examples-1-a1449236c308)

## Setup
Ensure that you have both Rust and Python3 installed.

Update to the latest version of Rust
```
rustup update
```

Add the Wasm target:
```
rustup target add wasm32-unknown-unknown
```

Install Rust dependencies:
```
cargo build --release --target wasm32-unknown-unknown
```

Install wasmer for Python:
```
python3.6 -m pip install wasmer
# Or, on some systems:
pip3 install wasmer
```

## Run it!
```
cd pywasm
python3 run_wasm_with_python.py
python3 run_flask_bench.py
```

If everything is working correctly, you should see output that take timing of the functions run using python-ext-wasm and pure Python.
