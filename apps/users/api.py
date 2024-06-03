from werkzeug.security import generate_password_hash
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from .models import User, user_schema
from apps.db import db


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
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        db.session.close()
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.close()
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
        access_token = create_access_token(identity=user.id)
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

    user_data = user_schema.dump(user)

    user_data.pop('password_hash', None)

    user_data['comentarios'] = [{'id': comentario.id, 'descricao': comentario.descricao} for comentario in
                                user.comentarios]
    user_data['avaliacoes'] = [{'id': avaliacao.id, 'valor': avaliacao.valor} for avaliacao in user.avaliacoes]

    return jsonify(user_data), 200


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
        db.session.commit()
        return user_schema.jsonify(user), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating user', 'error': str(e)}), 500


def delete_user(id_user):
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error deleting user', 'error': str(e)}), 500


