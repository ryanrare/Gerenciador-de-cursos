from werkzeug.security import generate_password_hash
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from .models import User, user_schema
from apps import db


def user_by_username(username):
    try:
        return User.query.filter_by(username=username).first()
    except Exception as e:
        print(e)
        return None


def post_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json.get('email')

    user = user_by_username(username)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'user already exists', 'data': result}), 409

    password_hash = generate_password_hash(password)

    user = User(username, email, password_hash)

    try:
        session = db.Session()
        session.add(user)
        session.commit()
        result = user_schema.dump(user)
        session.close()
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        session.rollback()
        session.close()
        return jsonify({'message': 'unable to create', 'data': {}}), 500


def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None


def login_with_jwt():
    username = request.json.get('username')
    password = request.json.get('password')

    user = authenticate_user(username, password)
    if user:
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


def get_users():
    users = User.query.all()
    users_data = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(users=users_data), 200


def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return user_schema.jsonify(user), 200


def update_user(id_user):
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    user.username = username if username else user.username
    user.email = email if email else user.email
    if password:
        user.password_hash = generate_password_hash(password)

    try:
        session = db.Session()
        session.commit()
        return user_schema.jsonify(user), 200
    except Exception as e:
        session = db.Session()
        session.rollback()
        return jsonify({'message': 'Error updating user', 'error': str(e)}), 500


def delete_user(id_user):
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    try:
        session = db.Session()
        session.delete(user)
        session.commit()
        return jsonify({'message': 'User deleted'}), 200
    except Exception as e:
        session = db.Session()
        session.rollback()
        return jsonify({'message': 'Error deleting user', 'error': str(e)}), 500
