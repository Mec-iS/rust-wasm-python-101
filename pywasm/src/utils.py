"""
Memory Allocation Utilities
"""
def allocate_bytes(instance, size=8):
    """Create a view for an instance"""
    mem = instance.memory
    funcname = f'uint{size}_view'
    return getattr(mem, funcname)()

def write_to_memory(bytestr, mem_view, offset=0):
    """Fill memory with values"""
    for i, c in enumerate(bytestr):
        mem_view[offset + i] = c
    return mem_view

def address_to_utf8(mem_view, address, length):
    """Read from address into UTF-8"""
    codes = mem_view[address:address+length]

    string_ = ''
    for i, c in enumerate(codes):
        string_ += chr(c)

    return string_.encode()
