from werkzeug.security import generate_password_hash
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from .models import User, user_schema
from apps import db


def user_by_username(username):
    try:
        return User.query.filter(User.username == username).one()
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

    pass_hash = generate_password_hash(password)
    user = User(username, email, pass_hash)

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
