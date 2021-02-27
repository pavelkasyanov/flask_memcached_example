from dependency_injector.wiring import inject, Provide
from flask import jsonify, request, Blueprint

from src.containers import Container
from src.services import FibonacciService

fibonachi_bp = Blueprint('fibonachi', __name__)


@fibonachi_bp.route('/fibonachi', methods=['GET'])
@inject
def get_fibonacci_seq(fibonacci_service: FibonacciService = Provide[Container.fibonacci_service]):
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
