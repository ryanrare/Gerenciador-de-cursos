from flask import jsonify, request
from . import users_bp
from .api import login_with_jwt, post_user, get_users, get_user, update_user, delete_user
from flask_jwt_extended import jwt_required


@users_bp.route('/')
@jwt_required()
def home():
    return get_users()


@users_bp.route('register/', methods=['POST'])
def post_users():
    return post_user()


@users_bp.route('login/', methods=['POST'])
def login():
    return login_with_jwt()


@users_bp.route('/<int:id>/', methods=['GET'])
@jwt_required()
def get_user_route(id):
    return get_user(id)


@users_bp.route('/<int:id>/', methods=['PUT'])
@jwt_required()
def update_user_route(id):
    return update_user(id)


@users_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_user_route(id):
    return delete_user(id)
