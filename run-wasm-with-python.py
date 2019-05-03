import timeit

from wasmer import Instance

from timing.src_py import *

path = 'target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'

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

        # some timing using popular functions
        t_py = timeit.timeit('(py_simple_add(n-1, n) for n in range(100, 1000))', number=10000)
        print('py add', t_py)

        t_wasm = timeit.timeit('(simple_add(n-1, n) for n in range(100, 1000))', number=10000)
        print('t_wasm add', t_wasm)

        t_py = timeit.timeit('(py_fibonacci(n) for n in range(100, 1000))', number=10000)
        print('py fibo', t_py)

        t_wasm = timeit.timeit('(fibonacci(n) for n in range(100, 1000))', number=10000)
        print('t_wasm fibo', t_wasm)

        t_py = timeit.timeit('(py_string_loop(str(n)*100) for n in range(100, 1000))', number=10000)
        print('py str loop', t_py)

        t_wasm = timeit.timeit('(loop_str(str(n)*100) for n in range(100, 1000))', number=10000)
        print('t_wasm str loop', t_wasm)

        t_py = timeit.timeit('(py_shapely_convex_hull() for n in range(100, 1000))', number=10000)
        print('py shapely convex hull', t_py)

        t_wasm = timeit.timeit('(rust_geo_convex_hull() for n in range(100, 1000))', number=10000)
        print('t_wasm rust-geo convex hull', t_wasm)

if __name__ == '__main__':
    run_test()
