from bson.objectid import ObjectId

def user_serializer(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }
