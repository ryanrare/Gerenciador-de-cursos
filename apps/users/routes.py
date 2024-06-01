from flask import jsonify, request
from . import users_bp
from .api import login_with_jwt, post_user
from flask_jwt_extended import jwt_required


@users_bp.route('/')
@jwt_required()
def home():
    return jsonify(message="Users API!")


@users_bp.route('register/', methods=['POST'])
def post_users():
    return post_user()


@users_bp.route('login/', methods=['POST'])
def login():
    return login_with_jwt()
