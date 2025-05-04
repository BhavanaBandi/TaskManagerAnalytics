from flask import current_app
import logging

# Function to get the latest analytics from the MongoDB collection
def get_latest_analytics():
    db = current_app.db  # Use the correct MongoDB connection reference
    analytics = db.analytics.find().sort("timestamp", -1).limit(1)
    
    if analytics.count() > 0:  # Check if there are any results
        result = analytics[0]
        logging.debug(f"Latest Analytics: {result}")
        return result
    else:
        logging.debug("No analytics data found")
        return {}  # Return empty data if no analytics found

# Function to serialize a task for easier JSON response
def serialize_task(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "priority": task["priority"],
        "due_date": task["due_date"],
        "completed": task["completed"]
    }
