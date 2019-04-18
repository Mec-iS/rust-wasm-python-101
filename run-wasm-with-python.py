from wasmer import Instance

path = 'target/wasm32-unknown-unknown/release/medium-xp.wasm'

with open(path, 'rb') as bytecode:
    wasm_bytes = bytecode.read()
    instance = Instance(wasm_bytes)
    result = instance.exports.simple_add(12, 12)

    print('Modules exported from Rust: ')
    print(instance.exports)  # this will print function's name
    print('call simple_add(12, 12): ')
    print(result)  # 24
