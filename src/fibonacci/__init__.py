from flask import Blueprint

fibonacci = Blueprint('fibonachi', __name__)

import src.fibonacci.controllers.fibonacci_controller
