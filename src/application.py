from flask import Flask

from .containers import Container
from .fibonacci import fibonacci


def create_app() -> Flask:
    container = Container()
    container.wire(modules=[fibonacci])

    app = Flask(__name__)
    app.container = container
    app.register_blueprint(fibonacci.fibonachi_bp)

    return app