import json


with open(
    "nutrition/nutrition_data.json",
    "r"
) as file:

    nutrition_db = json.load(file)


def get_nutrition(animal):

    return nutrition_db.get(
        animal,
        {}
    )