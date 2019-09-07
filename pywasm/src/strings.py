"""
Utilities to handle characters strings and strings encodings.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def address_to_utf8(mem_view, address, length):
    """Read from address into UTF-8"""
    codes = mem_view[address:address+length]

    string_ = ''
    for i, c in enumerate(codes):
        string_ += chr(c)

    return string_.encode()
