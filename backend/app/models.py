def serialize_task(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "priority": task["priority"],
        "due_date": task["due_date"],
        "completed": task["completed"]
    }
