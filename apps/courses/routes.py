from flask import request
from flask_jwt_extended import jwt_required
from .api import (get_all_cursos, create_curso, get_curso, update_curso, delete_curso,
                  get_curso_comentarios, create_curso_comentario, delete_curso_comentario,
                  get_curso_avaliacoes, create_curso_avaliacao, delete_curso_avaliacao,
                  get_curso_aulas, create_curso_aula, delete_curso_aula,
                  get_curso_trilhas, create_curso_trilha, delete_curso_trilha,
                  get_curso_users, add_logged_in_user_to_curso, remove_user_from_curso)
from . import courses_bp


@courses_bp.route('/', methods=['GET'])
@jwt_required()
def get_cursos_route():
    return get_all_cursos()


@courses_bp.route('/', methods=['POST'])
@jwt_required()
def create_curso_route():
    data = request.get_json()
    return create_curso(data)


@courses_bp.route('/<int:id>/', methods=['GET'])
@jwt_required()
def get_curso_route(id):
    return get_curso(id)


@courses_bp.route('/<int:id>/', methods=['PUT'])
@jwt_required()
def update_curso_route(id):
    data = request.get_json()
    return update_curso(id, data)


@courses_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_curso_route(id):
    return delete_curso(id)


@courses_bp.route('/<int:curso_id>/comentarios/', methods=['GET'])
@jwt_required()
def get_curso_comentarios_route(curso_id):
    return get_curso_comentarios(curso_id)


@courses_bp.route('/<int:curso_id>/comentarios/', methods=['POST'])
@jwt_required()
def create_curso_comentario_route(curso_id):
    return create_curso_comentario(curso_id)


@courses_bp.route('/<int:curso_id>/comentarios/<int:comentario_id>/', methods=['DELETE'])
@jwt_required()
def delete_curso_comentario_route(curso_id, comentario_id):
    return delete_curso_comentario(curso_id, comentario_id)


@courses_bp.route('/<int:curso_id>/avaliacoes/', methods=['GET'])
@jwt_required()
def get_avaliacoes(curso_id):
    return get_curso_avaliacoes(curso_id)


@courses_bp.route('/<int:curso_id>/avaliacoes/', methods=['POST'])
@jwt_required()
def add_avaliacao(curso_id):
    return create_curso_avaliacao(curso_id)


@courses_bp.route('/<int:curso_id>/avaliacoes/<int:avaliacao_id>/', methods=['DELETE'])
@jwt_required()
def remove_avaliacao(curso_id, avaliacao_id):
    return delete_curso_avaliacao(curso_id, avaliacao_id)


@courses_bp.route('/<int:curso_id>/aulas/', methods=['GET'])
@jwt_required()
def get_aulas(curso_id):
    return get_curso_aulas(curso_id)


@courses_bp.route('/<int:curso_id>/aulas/', methods=['POST'])
@jwt_required()
def add_aula(curso_id):
    return create_curso_aula(curso_id)


@courses_bp.route('/<int:curso_id>/aulas/<int:aula_id>/', methods=['DELETE'])
@jwt_required()
def remove_aula(curso_id, aula_id):
    return delete_curso_aula(curso_id, aula_id)


@courses_bp.route('/<int:curso_id>/trilhas/', methods=['GET'])
@jwt_required()
def get_curso_trilhas_route(curso_id):
    return get_curso_trilhas(curso_id)


@courses_bp.route('/<int:curso_id>/trilhas/', methods=['POST'])
@jwt_required()
def create_curso_trilha_route(curso_id):
    return create_curso_trilha(curso_id)


@courses_bp.route('/<int:curso_id>/trilhas/<int:trilha_id>/', methods=['DELETE'])
@jwt_required()
def delete_curso_trilha_route(curso_id, trilha_id):
    return delete_curso_trilha(curso_id, trilha_id)


@courses_bp.route('/<int:curso_id>/users/', methods=['GET'])
@jwt_required()
def get_curso_users_route(curso_id):
    return get_curso_users(curso_id)


@courses_bp.route('/<int:curso_id>/users/', methods=['POST'])
@jwt_required()
def add_logged_in_user_to_curso_route(curso_id):
    return add_logged_in_user_to_curso(curso_id)


@courses_bp.route('/<int:curso_id>/users/<int:user_id>/', methods=['DELETE'])
@jwt_required()
def remove_user_from_curso_route(curso_id, user_id):
    return remove_user_from_curso(curso_id, user_id)
