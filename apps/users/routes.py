from flask import jsonify
from . import users_bp


@users_bp.route('/')
def home():
    return jsonify(message="Users API!")
