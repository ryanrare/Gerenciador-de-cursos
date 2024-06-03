from flask_jwt_extended import jwt_required

from flasgger.utils import swag_from
from apps.utils.docs_endpoints_swwaguer import (get_user_response, update_user_response, delete_user_response,
                                                login_response, register_response, home_response)

from . import users_bp
from .api import login_with_jwt, post_user, get_users, get_user, update_user, delete_user


@users_bp.route('/')
@swag_from(register_response)
def home():
    return get_users()


@users_bp.route('register/', methods=['POST'])
@swag_from(home_response)
def post_users():
    return post_user()


@users_bp.route('login/', methods=['POST'])
@swag_from(login_response)
def login():
    return login_with_jwt()


@users_bp.route('/<int:id>/', methods=['GET'])
@jwt_required()
@swag_from(get_user_response)
def get_user_route(id):
    return get_user(id)


@users_bp.route('/<int:id>/', methods=['PUT'])
@jwt_required()
@swag_from(update_user_response)
def update_user_route(id):
    return update_user(id)


@users_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
@swag_from(delete_user_response)
def delete_user_route(id):
    return delete_user(id)
