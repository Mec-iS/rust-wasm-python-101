# rust-wasm-python-101

A basic example of calling Rust from Python used as example in thhe blogpost: [Rust-scales Python: Basic experiment](https://medium.com/@lorenzogotuned/rust-scales-python-function-d3b1d24351cd).

## Setup
Ensure that you have both Rust and Python3 installed.

Update to the latest version of Rust
```
rustup update
```

Add the WASM target:
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
python3 run-wasm-with-python.py
```

If everything is working correctly, you should see output that looks something like:
```
Modules exported from Rust:
["loop_str", "fibo", "simple_add"]
call simple_add(12, 12):
24
py add 0.006070989000000006
t_wasm add 0.005827948999999999
py fibo 0.005115728999999999
t_wasm fibo 0.004803907000000003
py str loop 0.00475766100000001
t_wasm str loop 0.004782752000000001
```
