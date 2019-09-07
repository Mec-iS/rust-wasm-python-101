import time

from flask import g, jsonify
from .__init__ import create_app

app = create_app()

@app.route("/fibo_wasm/<n>")
def fibo_wasm(n):
    n = int(n)

    fibo = app.wasm.exports.fibo

    if n < 25:
        try:
            result = fibo(n)
        except:
            return f'Cannot compute fibo of {n}', 400
    else:
        return 'Avoid hogging... n should be less than 25'

    diff = time.time() - g.start
    return jsonify({
        "result": result,
        "time": diff
        }), 200


@app.route("/fibo_py/<n>")
def fibo_py(n):
    n = int(n)

    from examples.scientific import py_fibonacci

    if n < 25:
        try:
            result = py_fibonacci(n)
        except:
            return f'Cannot compute fibo of {n}', 400
    else:
        return 'Avoid hogging... n should be less than 25'

    diff = time.time() - g.start
    return jsonify({
        "result": result,
        "time": diff
        }), 200


@app.route("/convexhull_wasm/<n>")
def convexhull_wasm(n=0):
    n = int(n)

    convex_hull = app.wasm.exports.rust_geo_convex_hull

    if n < 25:
        try:
            result = convex_hull()
        except:
            return f'Cannot compute convex_hull', 400
    else:
        return 'Avoid hogging... n should be less than 25'

    diff = time.time() - g.start
    return jsonify({
        "result": result,
        "time": diff
        }), 200


@app.route("/convexhull_py/<n>")
def convexhull_py(n=0):
    n = int(n)

    from examples.scientific import py_shapely_convex_hull

    if n < 25:
        try:
            result = py_shapely_convex_hull()
        except:
            return f'Cannot compute convex_hull', 400
    else:
        return 'Avoid hogging... n should be less than 25'

    diff = time.time() - g.start
    return jsonify({
        "result": result,
        "time": diff
        }), 200

@app.before_request
def before_request():
  g.start = time.time()
