from flask import jsonify
from . import avaliacao_bp

from flask import Blueprint, request
from .api import get_all_avaliacoes, create_avaliacao, get_avaliacao, update_avaliacao, delete_avaliacao


@avaliacao_bp.route('/', methods=['GET'])
def get_avaliacoes_route():
    return get_all_avaliacoes()


@avaliacao_bp.route('/', methods=['POST'])
def create_avaliacao_route():
    data = request.get_json()
    return create_avaliacao(data)


@avaliacao_bp.route('/<int:id>/', methods=['GET'])
def get_avaliacao_route(id):
    return get_avaliacao(id)


@avaliacao_bp.route('/<int:id>/', methods=['PUT'])
def update_avaliacao_route(id):
    data = request.get_json()
    return update_avaliacao(id, data)


@avaliacao_bp.route('/<int:id>/', methods=['DELETE'])
def delete_avaliacao_route(id):
    return delete_avaliacao(id)
