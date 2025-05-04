from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from .models import serialize_task, get_latest_analytics

routes = Blueprint('routes', __name__)  # Use a single blueprint

@routes.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    db = current_app.db
    user_id = get_jwt_identity()
    tasks = list(db.tasks.find({"user_id": user_id}))
    return jsonify([serialize_task(t) for t in tasks])

@routes.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    db = current_app.db
    user_id = get_jwt_identity()
    data = request.json
    task = {
        "title": data["title"],
        "description": data["description"],
        "priority": data["priority"],
        "due_date": data["due_date"],
        "completed": False,
        "user_id": user_id
    }
    db.tasks.insert_one(task)
    return jsonify({"msg": "Task created"}), 201

@routes.route('/analytics', methods=['GET'])
def fetch_analytics():
    try:
        analytics = get_latest_analytics()
        return jsonify(analytics), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
