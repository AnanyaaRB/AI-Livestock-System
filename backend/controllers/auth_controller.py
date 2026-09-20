from flask import request
from flask import jsonify

from models.user_model import UserModel

def register():

    data = request.json

    UserModel.create_user(
        data["username"],
        data["email"],
        data["password"]
    )

    return jsonify(
        {"message":"User Registered"}
    )