import timeit

from wasmer import Instance

from src_py import *

path = '../target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'

context = '''from wasmer import Instance
path = 'target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'
wasm_bytes = open(path, 'rb').read()
instance = Instance(wasm_bytes)
'''

def run_test():
    with open(path, 'rb') as bytecode:
        wasm_bytes = bytecode.read()
        instance = Instance(wasm_bytes)

        # print exported functions
        print("Modules exported from Rust: ")
        print(instance.exports)

        # assign functions
        simple_add = instance.exports.simple_add
        fibo = instance.exports.fibo
        loop_str = instance.exports.loop_str
        rust_geo_convex_hull = instance.exports.rust_geo_convex_hull

        # try a simple addition
        result = simple_add(12, 12)
        print("call simple_add(12, 12): ")
        print(result)


if __name__ == '__main__':
    run_test()
