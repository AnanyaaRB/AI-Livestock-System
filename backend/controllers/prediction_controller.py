import os

from flask import request
from flask import jsonify

from ai.predict import predict

from models.prediction_model import (
    PredictionModel
)

from config import UPLOAD_FOLDER


def predict_animal():

    image = request.files["image"]

    save_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(save_path)

    result = predict(save_path)

    PredictionModel.save_prediction(
        result["animal"],
        result["confidence"],
        save_path
    )

    return jsonify(result)