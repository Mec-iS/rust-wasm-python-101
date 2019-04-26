import timeit

from wasmer import Instance

path = 'target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm'

def add(a, b):
    return a + b

def fibonacci(n):
    i = 0
    nextterm = 1
    present = 1
    previous = 0

    while i < n:
        nextterm = present + previous
        present = previous
        previous = nextterm
        i = i + 1

    return nextterm

def string_loop(string):
    for s in string:
        s = s * 10

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

    # try a simple addition
    result = simple_add(12, 12)
    print("call simple_add(12, 12): ")
    print(result)

    # some timing using popular functions
    t_py = timeit.timeit('(add(n-1, n) for n in range(100, 1000))', number=10000)
    print('py add', t_py)

    t_wasm = timeit.timeit('(simple_add(n-1, n) for n in range(100, 1000))', number=10000)
    print(t_wasm)

    t_py = timeit.timeit('(fibonacci(n) for n in range(100, 1000))', number=10000)
    print('py fibo', t_py)

    t_wasm = timeit.timeit('(fibo(n) for n in range(100, 1000))', number=10000)
    print(t_wasm)

    t_py = timeit.timeit('(string_loop(n) for n in range(100, 1000))', number=10000)
    print('py str loop', t_py)

    t_wasm = timeit.timeit('(loop_str(n) for n in range(100, 1000))', number=10000)
    print(t_wasm)
