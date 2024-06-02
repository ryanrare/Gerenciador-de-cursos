from . import trilhas_bp

from flask import Blueprint, request
from .api import get_all_trilhas, create_trilha, get_trilha, update_trilha, delete_trilha


@trilhas_bp.route('/', methods=['GET'])
def get_trilhas_route():
    return get_all_trilhas()


@trilhas_bp.route('/', methods=['POST'])
def create_trilha_route():
    data = request.get_json()
    return create_trilha(data)


@trilhas_bp.route('/<int:id>/', methods=['GET'])
def get_trilha_route(id):
    return get_trilha(id)


@trilhas_bp.route('/<int:id>/', methods=['PUT'])
def update_trilha_route(id):
    data = request.get_json()
    return update_trilha(id, data)


@trilhas_bp.route('/<int:id>/', methods=['DELETE'])
def delete_trilha_route(id):
    return delete_trilha(id)
