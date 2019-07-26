import requests
import random
import json
from time import sleep

def test_fibo_wasm():
    from .app import app
    app.config['TESTING'] = True
    client = app.test_client()

    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/fibo_wasm/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    print('time fibo_wasm', time)

def test_fibo_py():
    from .app import app
    app.config['TESTING'] = True
    client = app.test_client()

    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/fibo_py/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    print('time fibo_py', time)

def test_convexhull_wasm():
    from .app import app
    app.config['TESTING'] = True
    client = app.test_client()

    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/convexhull_wasm/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    print('time convexhull_wasm', time)

def test_convexhull_py():
    from .app import app
    app.config['TESTING'] = True
    client = app.test_client()

    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/convexhull_py/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    print('time convexhull_py', time)
