"""
A simple test for Python strings
"""
def test_reverse(mem, func, bytestr):
    mem_view = mem.uint8_view()
    for i, c in enumerate(bytestr):
        mem_view[i] = c

    result = func(0, len(bytestr))

    codes = mem_view[result:result + len(bytestr)]

    string_ = ''
    for i, c in enumerate(codes):
        string_ += chr(c)

    return string_.encode()
