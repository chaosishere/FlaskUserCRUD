from flask import request, jsonify, Blueprint
from . import db
from .models import user_serializer
from .schemas import UserSchema, UserUpdateSchema
from bson.objectid import ObjectId
from pymongo import ReturnDocument

userslist = db.users

api = Blueprint('api', __name__)

user_schema = UserSchema()
# user_update_schema = UserUpdateSchema()

@api.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        users = userslist.find()
        return jsonify([user_serializer(user) for user in users]), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        error = user_schema.validate(data)

        if error:
            return jsonify(error), 400
        
        unique_user = userslist.find_one({"email": data["email"]})
        if unique_user:
            return jsonify({'message': 'Email is already in use'}), 400
        
        user = userslist.insert_one(data)
        inseted_user = userslist.find_one({"_id": user.inserted_id})
        return jsonify(user_serializer(inseted_user)), 201
    

@api.route( '/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_update_delete_user(id):
    if request.method == 'GET':
        user  = userslist.find_one({"_id": ObjectId(id)})
        
        if user:
            return jsonify(user_serializer(user)), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    
    elif request.method == 'PUT':
        data = request.get_json()
        error = user_schema.validate(data)

        if error:
            return jsonify(error), 400
        
        existing_user = userslist.find_one({"email": data["email"]})
        
        if existing_user and str(existing_user['_id']) != id:
            return jsonify({"message": "Email is already in use"}), 400    
        
        user = userslist.find_one_and_update({"_id": ObjectId(id)}, {"$set": data}, return_document=ReturnDocument.AFTER)

        if user:
            return jsonify(user_serializer(user)), 200
        else:
            return jsonify({'message': 'User not found'}), 404
        
    elif request.method == 'DELETE':
        user = userslist.delete_one({"_id": ObjectId(id)})

        if user.deleted_count :
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
        

        



