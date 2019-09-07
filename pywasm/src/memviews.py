"""
Utilities to handle Wasm Memory views.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def get_memory_view(instance, size=8):
    """Get a view of `size` from a Wasmer an instance"""
    mem = instance.memory
    funcname = f'uint{size}_view'
    return getattr(mem, funcname)()

def write_to_view(bytestr, mem_view, offset=0):
    """Fill memory with values from a bytestring starting at `offset`"""
    for i, c in enumerate(bytestr):
        mem_view[offset + i] = c
    return mem_view
