import random
import json
from time import sleep

import pytest
from structlog import get_logger

logger = get_logger()

@pytest.fixture
def client():
    from .app import app
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_fibo_wasm(client):
    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/fibo_wasm/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    logger.info('Time it', func='fibo_wasm', time=time)

def test_fibo_py(client):
    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/fibo_py/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    logger.info('Time it', func='fibo_py', time=time)

def test_convexhull_wasm(client):
    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/convexhull_wasm/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    logger.info('Time it', func='convexhull_wasm', time=time)

def test_convexhull_py(client):
    time = None
    for n in range(10000):
        i = random.choice(list(x for x in range (1,25)))
        rv = client.get(f'/convexhull_py/{i}')
        data = json.loads(rv.data)
        if time is None:
            time = data['time']
        else:
            time = time + data['time'] / 2

    logger.info('Time it', func='convexhull_py', time=time)
