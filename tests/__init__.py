import pytest

from src.app import create_app

flask_app = create_app(testing=True)


@pytest.fixture(scope='function')
def test_client():
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
