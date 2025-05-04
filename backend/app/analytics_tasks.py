from datetime import datetime
from pymongo import MongoClient
from celery_worker import celery
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["task_manager"]

@celery.task
def generate_analytics():
    total = db.tasks.count_documents({})
    completed = db.tasks.count_documents({"status": "completed"})
    overdue = db.tasks.count_documents({
        "due_date": {"$lt": datetime.utcnow()},
        "status": {"$ne": "completed"}
    })

    metrics = {
        "timestamp": datetime.utcnow(),
        "total_tasks": total,
        "completed_tasks": completed,
        "overdue_tasks": overdue,
        "completion_rate": round((completed / total) * 100, 2) if total > 0 else 0
    }

    db.analytics.insert_one(metrics)
    return metrics
