from datetime import datetime
import timeit
import os
from os.path import join, dirname, abspath
import csv

import wasmer
from wasmer import Instance

from examples.scientific import *

path = join(dirname(dirname(abspath(__file__))), 'target', 'wasm32-unknown-unknown', 'release', 'rust_wasm_python_101.wasm')

print('>>>', path)

context = f'''
from wasmer import Instance
path = "{path}"
wasm_bytes = open(path, 'rb').read()
instance = Instance(wasm_bytes)
simple_add = instance.exports.simple_add
'''

def run_timing():
    with open(path, 'rb') as bytecode:
        wasm_bytes = bytecode.read()
        instance = Instance(wasm_bytes)
        # assign functions
        simple_add = instance.exports.simple_add
        fibo = instance.exports.fibo
        rust_geo_convex_hull = instance.exports.rust_geo_convex_hull

        # print exported functions
        print("Modules exported from Rust: ")
        print(instance.exports)

        # define metadata in results
        from collections import OrderedDict
        results = OrderedDict()
        results['timestap'] = str(datetime.now())
        results['python_wasmer_v'] = f'{wasmer.__version__}|{wasmer.__core_version__}'

        import subprocess
        rustc_v = subprocess.check_output(['rustc', '--version']).decode().rstrip()
        results['rustc_v'] = rustc_v

        results['data'] = {}

        t_py = timeit.timeit('[py_simple_add(n-1, n) for n in range(100, 1000)]', number=10000, setup='from examples.scientific import py_simple_add')
        print('py add', t_py)

        t_wasm = timeit.timeit('[simple_add(n-1, n) for n in range(100, 1000)]', number=10000, setup=context+'simple_add = instance.exports.simple_add')
        print('t_wasm add', t_wasm)
        results['data']['simple_add'] = { 'py': t_py, 'wasm': t_wasm }

        t_py = timeit.timeit('[py_fibonacci(n) for n in range(100, 1000)]', number=1000, setup='from examples.scientific import py_fibonacci')
        print('py fibo', t_py)

        t_wasm = timeit.timeit('[fibo(n) for n in range(100, 1000)]', number=1000, setup=context+'fibo = instance.exports.fibo')
        print('t_wasm fibo', t_wasm)
        results['data']['fibonacci'] = { 'py': t_py, 'wasm': t_wasm }

        t_py = timeit.timeit('[py_shapely_convex_hull() for n in range(100, 1000)]', number=1000, setup='from examples.scientific import py_shapely_convex_hull')
        print('py shapely convex hull', t_py)

        t_wasm = timeit.timeit('[rust_geo_convex_hull() for n in range(100, 1000)]', number=1000, setup=context+'rust_geo_convex_hull = instance.exports.rust_geo_convex_hull')
        print('t_wasm rust-geo convex hull', t_wasm)
        results['data']['convex_hull'] = { 'py': t_py, 'wasm': t_wasm }

        # CSV file
        csv_file = join(dirname(__file__), 'timing', 'data', 'timing.csv')
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=results.keys())
            if not file_exists:
                writer.writeheader()
                file_exists = True
            writer.writerow(results)

if __name__ == '__main__':
    run_timing()
