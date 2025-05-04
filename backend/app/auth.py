from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    db = current_app.db
    data = request.json
    if db.users.find_one({"email": data["email"]}):
        return jsonify({"msg": "User already exists"}), 409

    user = {
        "email": data["email"],
        "password": generate_password_hash(data["password"])
    }
    db.users.insert_one(user)
    return jsonify({"msg": "User created"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    db = current_app.db
    data = request.json
    user = db.users.find_one({"email": data["email"]})
    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user["_id"]))
    return jsonify(access_token=token)
