import logging

from flask import Flask

from .containers import Container
from .fibonacci import fibonacci


def create_app() -> Flask:
    app = Flask(__name__)

    container = Container()
    container.config.host.from_env('CACHE_HOST')
    container.config.port.from_env('CACHE_PORT')

    container.wire(modules=[fibonacci])

    app.container = container
    app.register_blueprint(fibonacci.fibonachi_bp)

    return app