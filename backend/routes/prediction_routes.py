from flask import Blueprint

from controllers.prediction_controller import (
    predict_animal
)


prediction_bp = Blueprint(
    "prediction",
    __name__
)


prediction_bp.route(
    "/predict",
    methods=["POST"]
)(predict_animal)