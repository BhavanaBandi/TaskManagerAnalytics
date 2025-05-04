from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from .models import serialize_task

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    db = current_app.db
    user_id = get_jwt_identity()
    tasks = list(db.tasks.find({"user_id": user_id}))
    return jsonify([serialize_task(t) for t in tasks])

@task_bp.route('/tasks', methods=['POST'])
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
