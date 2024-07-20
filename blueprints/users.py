from flask import Blueprint, jsonify, request
from bson import ObjectId
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from flask import current_app

load_dotenv()

client = MongoClient(os.getenv("MONGODB_ATLAS_URI"))
db = client[os.getenv("MONGODB_ATLAS_DATABASE_NAME")]  
collection = db[os.getenv("MONGODB_ATLAS_COLLECTION_NAME")]

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users/', methods=['POST'])
def add_user():
    current_app.logger.info('User is being added')
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    try:
        collection.insert_one(user)
        return jsonify({'message': f'User {name} added successfully!'})
    except Exception as e:
        current_app.logger.error(f'Error adding user: {e}')
        return jsonify({'message': f'Error adding user: {e}'}), 500

@users_blueprint.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = collection.find_one({'_id': ObjectId(id)})
        user = [{'_id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']}]
        current_app.logger.info(f'User {id} retrieved successfully')
        return jsonify({'user': user})
    except Exception as e:
        current_app.logger.error(f'Error getting user: {e}')
        return jsonify({'message': f'Error getting user: {e}'}), 500
   

@users_blueprint.route('/users/', methods=['GET'])
def get_all_users():
    try:
        users = list(collection.find())
        users = [{'_id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']} for user in users]
        current_app.logger.info(f'All users retrieved successfully')
        return jsonify({'users': users})
    except Exception as e:
        current_app.logger.error(f'Error getting users: {e}')
        return jsonify({'message': f'Error getting users: {e}'}), 500

@users_blueprint.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    try:
        collection.update_one({'_id': ObjectId(id)}, {'$set': user})
        current_app.logger.info(f'User {id} updated successfully')
        return jsonify({'message': f'User {id} updated successfully!'})
    except Exception as e:
        current_app.logger.error(f'Error updating user: {e}')
        return jsonify({'message': f'Error updating user: {e}'}), 500

@users_blueprint.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        collection.delete_one({'_id': ObjectId(id)})
        current_app.logger.info(f'User {id} deleted successfully')
        return jsonify({'message': f'User {id} deleted successfully!'})
    except Exception as e:
        current_app.logger.error(f'Error deleting user: {e}')
        return jsonify({'message': f'Error deleting user: {e}'}), 500