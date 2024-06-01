from flask import jsonify
from . import users_bp
from .api import post_user


@users_bp.route('/')
def home():
    return jsonify(message="Users API!")


@users_bp.route('register/', methods=['POST'])
def post_users():
    return post_user()
