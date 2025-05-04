

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    CORS(app)
    jwt = JWTManager(app)

    client = MongoClient("mongodb://localhost:27017/")
    app.db = client["taskmanager"]

    from .routes import task_bp
    from .auth import auth_bp
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)

    return app
