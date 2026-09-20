from ai.preprocess import preprocess_image
from ai.animal_classifier import classify

def predict(path):

    image = preprocess_image(path)

    return classify(image)