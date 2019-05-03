from shapely.geometry import MultiPoint

def py_simple_add(a, b):
    return a + b

def py_fibonacci(n):
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

def py_string_loop(string):
    for s in string:
        s = s * 10

def py_shapely_convex_hull():
    shp = [
       (0.0, 0.0),
       (4.0, 0.0),
       (4.0, 1.0),
       (1.0, 1.0),
       (1.0, 4.0),
       (0.0, 4.0),
       (0.0, 0.0),
    ]

    MultiPoint(shp).convex_hull