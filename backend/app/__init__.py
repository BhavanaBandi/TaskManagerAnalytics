from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from .routes import routes  

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    
    CORS(app)
    jwt = JWTManager(app)

    
    client = MongoClient("mongodb://localhost:27017/")
    app.db = client["taskmanager"]  
    
    app.register_blueprint(routes)

    return app


