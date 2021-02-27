from flask import Blueprint

fibonacci = Blueprint('fibonacci', __name__)

import src.fibonacci.fibonacci_controller
