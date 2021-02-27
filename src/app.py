from flask import Flask

from src.fibonacci import fibonacci

app = Flask(__name__)


def create_app(testing: bool = False):
    app.config['TESTING'] = testing

    app.register_blueprint(fibonacci, url_prefix='/fibonachi')

    

    return app


def configure(binder):
    pass
