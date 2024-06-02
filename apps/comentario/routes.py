from . import comentario_bp

from flask import Blueprint, request
from .api import get_all_comentarios, create_comentario, get_comentario, update_comentario, delete_comentario


@comentario_bp.route('/', methods=['GET'])
def get_comentarios_route():
    return get_all_comentarios()


@comentario_bp.route('/', methods=['POST'])
def create_comentario_route():
    data = request.get_json()
    return create_comentario(data)


@comentario_bp.route('/<int:id>/', methods=['GET'])
def get_comentario_route(id):
    return get_comentario(id)


@comentario_bp.route('/<int:id>/', methods=['PUT'])
def update_comentario_route(id):
    data = request.get_json()
    return update_comentario(id, data)


@comentario_bp.route('/<int:id>/', methods=['DELETE'])
def delete_comentario_route(id):
    return delete_comentario(id)
