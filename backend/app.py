from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.prediction_routes import prediction_bp
from routes.nutrition_routes import nutrition_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(prediction_bp)
app.register_blueprint(nutrition_bp)

@app.route("/")
def home():
    return {
        "message":
        "AI Livestock Backend Running"
    }

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )