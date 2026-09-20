import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "livestock_model.keras"
)

DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "livestock.db"
)