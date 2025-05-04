from flask import current_app

def get_latest_analytics():
    db = current_app.config["DB"]
    return db.analytics.find().sort("timestamp", -1).limit(1)[0]


def serialize_task(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "priority": task["priority"],
        "due_date": task["due_date"],
        "completed": task["completed"]
    }
