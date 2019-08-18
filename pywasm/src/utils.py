"""
Memeory Allocation Utilities
"""
def allocate_bytes(instance, size=8):
    """Create a view for an instance"""
    mem = instance.memory
    return mem.uint8_view()

def write_to_memory(bytestr, mem_view, offset=0):
    """Fill memory with values"""
    for i, c in enumerate(bytestr):
        mem_view[i] = c
    return mem_view

def address_to_utf8(mem_view, address, length):
    """Read from address into UTF-8"""
    codes = mem_view[address:address+length]

    string_ = ''
    for i, c in enumerate(codes):
        string_ += chr(c)

    return string_.encode()
