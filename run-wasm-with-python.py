import timeit

from wasmer import Instance

from timing.src_py import *

path = 'target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'

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

        #some timing using popular functions
        t_py = timeit.timeit('[py_simple_add(n-1, n) for n in range(100, 1000)]', number=10000, setup='from timing.src_py import py_simple_add')
        print('py add', t_py)

        t_wasm = timeit.timeit('[simple_add(n-1, n) for n in range(100, 1000)]', number=10000, setup=context+'simple_add = instance.exports.simple_add')
        print('t_wasm add', t_wasm)

        t_py = timeit.timeit('[py_fibonacci(n) for n in range(100, 1000)]', number=1000, setup='from timing.src_py import py_fibonacci')
        print('py fibo', t_py)

        t_wasm = timeit.timeit('[fibo(n) for n in range(100, 1000)]', number=1000, setup=context+'fibo = instance.exports.fibo')
        print('t_wasm fibo', t_wasm)

        # t_py = timeit.timeit('[py_string_loop(str(n)*100) for n in range(100, 1000)]', number=1000, setup='from timing.src_py import py_string_loop')
        # print('py str loop', t_py)
        #
        # t_wasm = timeit.timeit('[loop_str(str(n)*100) for n in range(100, 1000)]', number=1000, setup=context+'loop_str = instance.exports.loop_str')
        # print('t_wasm str loop', t_wasm)

        t_py = timeit.timeit('[py_shapely_convex_hull() for n in range(100, 1000)]', number=1000, setup='from timing.src_py import py_shapely_convex_hull')
        print('py shapely convex hull', t_py)

        t_wasm = timeit.timeit('[rust_geo_convex_hull() for n in range(100, 1000)]', number=1000, setup=context+'rust_geo_convex_hull = instance.exports.rust_geo_convex_hull')
        print('t_wasm rust-geo convex hull', t_wasm)

if __name__ == '__main__':
    run_test()
