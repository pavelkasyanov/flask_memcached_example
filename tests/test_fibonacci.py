import json
from unittest import mock
import pytest

from src.repositories import MemcachedRepository
from src.application import create_app

FIBONACCI_PREFIX = '/fibonachi'


@pytest.fixture
def app():
    app = create_app()
    yield app
    app.container.unwire()



def test_invalid_request_params(client, app):
    data = {
        'from': -1,
        'to': 5
    }
    response = client.get(FIBONACCI_PREFIX, query_string=data)

    assert response.status_code == 400


def test_invalid_sequence_range(client, app):
    data = {
        'from': 5,
        'to': 3
    }
    response = client.get(FIBONACCI_PREFIX, query_string=data)

    assert response.status_code == 400


def test_success_json_response(client, app):
    cache_repository_mock = mock.Mock(spec=MemcachedRepository)
    cache_repository_mock.get_cache_seq.return_value = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                                                        987,
                                                        1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]

    data = {
        'from': 3,
        'to': 5
    }
    with app.container.cache_repository.override(cache_repository_mock):
        response = client.get(FIBONACCI_PREFIX, query_string=data)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'


def test_success_sequence(client, app):
    cache_repository_mock = mock.Mock(spec=MemcachedRepository)
    cache_repository_mock.get_cache_seq.return_value = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                                                        987,
                                                        1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]

    data = {
        'from': 3,
        'to': 5
    }
    with app.container.cache_repository.override(cache_repository_mock):
        response = client.get(FIBONACCI_PREFIX, query_string=data)

    assert response.status_code == 200

    succcess_seq = [3, 5]

    data = json.loads(response.data)

    assert succcess_seq == data
