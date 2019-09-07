try:
    from pywasm.src.utils import allocate_bytes, write_to_memory, address_to_utf8
except:
    import sys
    from os.path import abspath, dirname
    print(abspath(dirname(dirname(dirname(__file__)))))
    sys.path.insert(0, abspath(dirname(dirname(dirname(dirname(__file__))))))
    from pywasm.src.utils import allocate_bytes, write_to_memory, address_to_utf8

def py_reverse_string(string):
    return string[::1]

def test_reverse(instance, func, bytestr):
    """A simple string reversing test using Wasm memory"""
    mem_view = allocate_bytes(instance)

    mem_view = write_to_memory(bytestr, mem_view, offset=0)

    result = func(0, len(bytestr))

    return address_to_utf8(mem_view, result, len(bytestr))
