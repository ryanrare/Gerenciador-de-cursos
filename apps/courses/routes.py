from flask import Blueprint, request
from .api import get_all_cursos, create_curso, get_curso, update_curso, delete_curso
from . import courses_bp


@courses_bp.route('/', methods=['GET'])
def get_cursos_route():
    return get_all_cursos()


@courses_bp.route('/', methods=['POST'])
def create_curso_route():
    data = request.get_json()
    return create_curso(data)


@courses_bp.route('/<int:id>/', methods=['GET'])
def get_curso_route(id):
    return get_curso(id)


@courses_bp.route('/<int:id>/', methods=['PUT'])
def update_curso_route(id):
    data = request.get_json()
    return update_curso(id, data)


@courses_bp.route('/<int:id>/', methods=['DELETE'])
def delete_curso_route(id):
    return delete_curso(id)
