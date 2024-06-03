from . import trilhas_bp
from apps.utils.docs_endpoints_swwaguer import (
    get_all_trilhas_response, create_trilha_response, get_trilha_response, update_trilha_response, delete_trilha_response,
    get_trilha_comentarios_response, create_trilha_comentario_response, delete_trilha_comentario_response,
    get_trilha_avaliacoes_response, create_trilha_avaliacao_response, delete_trilha_avaliacao_response,
    get_trilha_cursos_response, create_trilha_curso_response, delete_trilha_curso_response,
    get_trilha_aulas_response, create_trilha_aula_response, delete_trilha_aula_response,
    get_trilha_users_response, add_trilha_user_response, remove_trilha_user_response
    )

from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
from flask import request

from .api import (get_all_trilhas, create_trilha, get_trilha, update_trilha, delete_trilha,
                  get_trilha_comentarios, create_trilha_comentario, delete_trilha_comentario,
                  get_trilha_avaliacoes, create_trilha_avaliacao, delete_trilha_avaliacao,
                  get_trilha_cursos, create_trilha_curso, delete_trilha_curso,
                  get_trilha_aulas, create_trilha_aula, delete_trilha_aula,
                  add_logged_in_user_to_trilha, get_trilha_users, remove_user_from_trilha)


@trilhas_bp.route('/', methods=['GET'])
@jwt_required()
@swag_from(get_all_trilhas_response)
def get_trilhas_route():
    return get_all_trilhas()


@trilhas_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(create_trilha_response)
def create_trilha_route():
    data = request.get_json()
    return create_trilha(data)


@trilhas_bp.route('/<int:id>/', methods=['GET'])
@jwt_required()
@swag_from(get_trilha_response)
def get_trilha_route(id):
    return get_trilha(id)


@trilhas_bp.route('/<int:id>/', methods=['PUT'])
@jwt_required()
@swag_from(update_trilha_response)
def update_trilha_route(id):
    data = request.get_json()
    return update_trilha(id, data)


@trilhas_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
@swag_from(delete_trilha_response)
def delete_trilha_route(id):
    return delete_trilha(id)


@trilhas_bp.route('/<int:trilha_id>/comentarios/', methods=['GET'])
@jwt_required()
@swag_from(get_trilha_comentarios_response)
def get_trilha_comentarios_route(trilha_id):
    return get_trilha_comentarios(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/comentarios/', methods=['POST'])
@jwt_required()
@swag_from(create_trilha_comentario_response)
def create_trilha_comentario_route(trilha_id):
    return create_trilha_comentario(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/comentarios/<int:comentario_id>/', methods=['DELETE'])
@jwt_required()
@swag_from(delete_trilha_comentario_response)
def delete_trilha_comentario_route(trilha_id, comentario_id):
    return delete_trilha_comentario(trilha_id, comentario_id)


@trilhas_bp.route('/<int:trilha_id>/avaliacoes/', methods=['POST'])
@jwt_required()
@swag_from(create_trilha_avaliacao_response)
def create_avaliacao_route(trilha_id):
    return create_trilha_avaliacao(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/avaliacoes/', methods=['GET'])
@jwt_required()
@swag_from(get_trilha_avaliacoes_response)
def get_avaliacoes_route(trilha_id):
    return get_trilha_avaliacoes(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/avaliacoes/<int:avaliacao_id>/', methods=['DELETE'])
@jwt_required()
@swag_from(delete_trilha_avaliacao_response)
def delete_avaliacao_route(trilha_id, avaliacao_id):
    return delete_trilha_avaliacao(trilha_id, avaliacao_id)


@trilhas_bp.route('/<int:trilha_id>/cursos/', methods=['POST'])
@jwt_required()
@swag_from(create_trilha_curso_response)
def create_curso_route(trilha_id):
    return create_trilha_curso(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/cursos/', methods=['GET'])
@jwt_required()
@swag_from(get_trilha_cursos_response)
def get_cursos_route(trilha_id):
    return get_trilha_cursos(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/cursos/<int:curso_id>/', methods=['DELETE'])
@jwt_required()
@swag_from(delete_trilha_curso_response)
def delete_curso_route(trilha_id, curso_id):
    return delete_trilha_curso(trilha_id, curso_id)


@trilhas_bp.route('/<int:trilha_id>/aulas/', methods=['POST'])
@jwt_required()
@swag_from(create_trilha_aula_response)
def create_aula_route(trilha_id):
    return create_trilha_aula(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/aulas/', methods=['GET'])
@jwt_required()
@swag_from(get_trilha_aulas_response)
def get_aulas_route(trilha_id):
    return get_trilha_aulas(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/aulas/<int:aula_id>/', methods=['DELETE'])
@jwt_required()
@swag_from(delete_trilha_aula_response)
def delete_aula_route(trilha_id, aula_id):
    return delete_trilha_aula(trilha_id, aula_id)


@trilhas_bp.route('/<int:trilha_id>/users/', methods=['POST'])
@jwt_required()
@swag_from(add_trilha_user_response)
def add_user_route(trilha_id):
    return add_logged_in_user_to_trilha(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/users/', methods=['GET'])
@jwt_required()
@swag_from(get_trilha_users_response)
def get_users_route(trilha_id):
    return get_trilha_users(trilha_id)


@trilhas_bp.route('/<int:trilha_id>/users/<int:user_id>/', methods=['DELETE'])
@jwt_required()
@swag_from(remove_trilha_user_response)
def remove_user_route(trilha_id, user_id):
    return remove_user_from_trilha(trilha_id, user_id)
