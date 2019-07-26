import sys
import os
from os.path import dirname, join

from flask import Flask

root_path = dirname(dirname(dirname(__file__)))

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # load the Wasm binary for Flask app
    from wasmer import Instance
    path = join(dirname(root_path), 'target/wasm32-unknown-unknown/release/rust_wasm_python_101.wasm')
    wasm_bytes = open(path, 'rb').read()
    app.wasm = Instance(wasm_bytes)

    return app
