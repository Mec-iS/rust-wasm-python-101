from datetime import datetime
import timeit
import os
from os.path import join, dirname
import csv

import wasmer
from wasmer import Instance

from src_py import *

path = 'target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'


def run_timing():
    with open(path, 'rb') as bytecode:
        wasm_bytes = bytecode.read()
        instance = Instance(wasm_bytes)
        # assign functions
        simple_add = instance.exports.simple_add
        fibo = instance.exports.fibo
        loop_str = instance.exports.loop_str
        rust_geo_convex_hull = instance.exports.rust_geo_convex_hull

        # print exported functions
        print("Modules exported from Rust: ")
        print(instance.exports)

        # define metadata in results
        from collections import OrderedDict
        results = OrderedDict()
        results['timestap'] = str(datetime.now())
        results['python_wasmer_v'] = wasmer.__version__
        results['rustc_v'] = open(join(dirname(__file__), 'CONFIG'), 'r').read()
        results['data'] = {}

        # CSV file
        csv_file = join(dirname(__file__), 'data', 'timing.csv')
        file_exists = os.path.isfile(csv_file)

        for _ in range(100):
            # some timing using popular functions
            t_py = timeit.timeit('(py_simple_add(n-1, n) for n in range(100, 1000))', number=10000)
            t_wasm = timeit.timeit('(simple_add(n-1, n) for n in range(100, 1000))', number=10000)
            results['data']['simple_add'] = { 'py': t_py, 'wasm': t_wasm }

            t_py = timeit.timeit('(py_fibonacci(n) for n in range(100, 1000))', number=10000)
            t_wasm = timeit.timeit('(fibonacci(n) for n in range(100, 1000))', number=10000)
            results['data']['fibonacci'] = { 'py': t_py, 'wasm': t_wasm }

            t_py = timeit.timeit('(py_string_loop(str(n)*100) for n in range(100, 1000))', number=10000)
            t_wasm = timeit.timeit('(loop_str(str(n)*100) for n in range(100, 1000))', number=10000)
            results['data']['string_loop'] = { 'py': t_py, 'wasm': t_wasm }

            t_py = timeit.timeit('(py_shapely_convex_hull() for n in range(100, 1000))', number=10000)
            t_wasm = timeit.timeit('(rust_geo_convex_hull() for n in range(100, 1000))', number=10000)
            results['data']['convex_hull'] = { 'py': t_py, 'wasm': t_wasm }

            with open(csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=results.keys())
                if not file_exists:
                    writer.writeheader()
                    file_exists = True
                writer.writerow(results)

if __name__ == '__main__':
    run_timing()
