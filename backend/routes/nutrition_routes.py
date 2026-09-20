from flask import Blueprint

from controllers.nutrition_controller import (
    nutrition
)

nutrition_bp = Blueprint(
    "nutrition",
    __name__
)

nutrition_bp.route(
    "/nutrition/<animal>"
)(nutrition)