from tests import test_client

FIBONACCI_PREFIX = '/fibonachi'


def test_invalid_request_params(test_client):
    data = {
        'from': -1,
        'to': 5
    }
    response = test_client.get(FIBONACCI_PREFIX, query_string=data)

    assert response.status_code == 400


def test_invalid_sequence_range(test_client):
    data = {
        'from': 5,
        'to': 3
    }
    response = test_client.get(FIBONACCI_PREFIX, query_string=data)

    assert response.status_code == 400
