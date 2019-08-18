from shapely.geometry import MultiPoint

def py_simple_add(a, b):
    return a + b

def py_fibonacci(n):
    """https://stackoverflow.com/a/52133289/2536357"""
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

def py_shapely_convex_hull(shp=None):
    if shp is None:
        shp = tuple([
           (0.0, 0.0),
           (4.0, 0.0),
           (4.0, 1.0),
           (1.0, 1.0),
           (1.0, 4.0),
           (0.0, 4.0),
           (0.0, 0.0),
        ])

    MultiPoint(shp).convex_hull

def py_reverse_string(string):
    return string[::1]

try:
    from pywasm.src.utils import allocate_bytes, write_to_memory, address_to_utf8
except:
    import sys
    from os.path import abspath, dirname
    sys.path.insert(0, abspath(dirname(dirname(dirname(__file__)))))
    from pywasm.src.utils import allocate_bytes, write_to_memory, address_to_utf8

def test_reverse(instance, func, bytestr):
    """A simple string reversing test using Wasm memory"""
    mem_view = allocate_bytes(instance)

    mem_view = write_to_memory(bytestr, mem_view, offset=0)

    result = func(0, len(bytestr))

    return address_to_utf8(mem_view, result, len(bytestr))
