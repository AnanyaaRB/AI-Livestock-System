from ai.animal_classifier import classify_animal

def predict(image_path):

    result = classify_animal(image_path)

    return result