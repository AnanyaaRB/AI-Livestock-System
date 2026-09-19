import random

ANIMALS = [
    "Cow",
    "Buffalo",
    "Goat",
    "Sheep"
]

def classify_animal(image_path):
    prediction = random.choice(ANIMALS)

    confidence = round(random.uniform(85, 99), 2)

    return {
        "animal": prediction,
        "confidence": confidence
    }