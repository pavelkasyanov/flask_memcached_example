from flask import jsonify, request

from src.fibonacci import fibonacci
from src.fibonacci.services.fibonacci_service import FibonacciService


@fibonacci.route('', methods=['GET'])
def get_fibonacci_seq(fibonacci_service: FibonacciService):
    try:
        seq_start = int(request.args.get('from'))
        seq_end = int(request.args.get('to'))

        if seq_start < 0 or seq_end < 0:
            raise ValueError(f"seq_start({seq_start}) < 0 or seq_end({seq_end}) < 0")
        if seq_start > seq_end:
            raise ValueError(f"seq_start > seq_end: {seq_start} > {seq_end}")
    except Exception as ex:
        return jsonify(str(ex)), 400

    result_seq = fibonacci_service.get_fibonacci_seq(seq_start, seq_end)
    return jsonify(result_seq), 200

