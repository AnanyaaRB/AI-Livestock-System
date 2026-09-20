from flask import jsonify

from nutrition.nutrition_service import (
    get_nutrition
)

def nutrition(animal):

    return jsonify(
        get_nutrition(animal)
    )