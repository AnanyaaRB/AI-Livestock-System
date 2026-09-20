from tensorflow.keras.models import load_model
from config import MODEL_PATH

model = load_model(MODEL_PATH)

classes = [
    "Buffalo",
    "Cow",
    "Goat",
    "Sheep"
]

def classify(image):

    prediction = model.predict(image)

    idx = prediction.argmax()

    return {
        "animal": classes[idx],
        "confidence": float(
            prediction[0][idx] * 100
        )
    }