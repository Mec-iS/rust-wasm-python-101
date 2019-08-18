import timeit

from wasmer import Instance

from src_py import *

path = '../target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'

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
        reverse_string = instance.exports.reverse_string

        # try a simple addition
        result = simple_add(12, 12)
        print("call simple_add(12, 12): ")
        print(result)

        from src_py.str_alloc import test_reverse
        test_str = b'Test sTRing'
        result = test_reverse(instance.memory, reverse_string, test_str)

        print(f'Reversing {test_str} >')
        print(result)


if __name__ == '__main__':
    run_test()
