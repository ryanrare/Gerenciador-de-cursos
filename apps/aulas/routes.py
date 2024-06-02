from flask import jsonify, request
from . import aulas_bp

from .api import (
    get_all_aulas,
    create_aula,
    get_aula,
    update_aula,
    delete_aula
)
from flask_jwt_extended import jwt_required


@aulas_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_aulas_route():
    return get_all_aulas()


@aulas_bp.route('/', methods=['POST'])
@jwt_required()
def create_aula_route():
    data = request.json
    return create_aula(data)


@aulas_bp.route('/<int:id>/', methods=['GET'])
@jwt_required()
def get_aula_route(id):
    return get_aula(id)


@aulas_bp.route('/<int:id>/', methods=['PUT'])
@jwt_required()
def update_aula_route(id):
    data = request.json
    return update_aula(id, data)


@aulas_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_aula_route(id):
    return delete_aula(id)
