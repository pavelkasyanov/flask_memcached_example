from flask import jsonify

from . import fibonacci


@fibonacci.route('/', methods=['GET'])
def get_fibonacci_seq():
    result_seq = []
    return jsonify(result_seq), 200
