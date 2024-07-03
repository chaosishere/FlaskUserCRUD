from bson.objectid import ObjectId
import datetime

def user_serializer(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "created_at": user["_id"].generation_time.isoformat()
    }
