import json
import os

BASE_DIR = os.path.dirname(__file__)

with open(
    os.path.join(BASE_DIR, "nutrition_data.json"),
    "r",
    encoding="utf-8"
) as f:
    nutrition_db = json.load(f)


def get_nutrition(animal):
    animal = animal.lower()

    if animal in nutrition_db:
        return nutrition_db[animal]

    return {
        "message": "Animal not found"
    }