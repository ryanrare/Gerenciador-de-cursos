from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from .models import Trilha
from apps.avaliacao.models import Avaliacao
from apps.comentario.models import Comentario
from apps.courses.models import Curso
from apps.aulas.models import Aula
from apps.users.models import User
from apps.db import db

"""CRUD DE TRILHA"""


def get_all_trilhas():
    trilhas = Trilha.query.all()
    trilhas_data = [{'id': trilha.id, 'titulo': trilha.titulo, 'descricao': trilha.descricao} for trilha in trilhas]
    return jsonify(trilhas=trilhas_data), 200


def create_trilha(data):
    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo or not descricao:
        return jsonify({'message': 'Missing data'}), 400

    nova_trilha = Trilha(titulo=titulo, descricao=descricao)
    db.session.add(nova_trilha)
    db.session.commit()

    return jsonify({'id': nova_trilha.id, 'titulo': nova_trilha.titulo, 'descricao': nova_trilha.descricao}), 201


def get_trilha(id):
    trilha = Trilha.query.get(id)
    if trilha is None:
        return jsonify({'message': 'Trilha not found'}), 404
    return jsonify({'id': trilha.id, 'titulo': trilha.titulo, 'descricao': trilha.descricao}), 200


def update_trilha(id, data):
    trilha = Trilha.query.get(id)
    if trilha is None:
        return jsonify({'message': 'Trilha not found'}), 404

    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo or not descricao:
        return jsonify({'message': 'Missing data'}), 400

    trilha.titulo = titulo
    trilha.descricao = descricao
    db.session.commit()

    return jsonify({'message': 'Trilha updated successfully'}), 200


def delete_trilha(id):
    trilha = Trilha.query.get(id)
    if trilha is None:
        return jsonify({'message': 'Trilha not found'}), 404

    db.session.delete(trilha)
    db.session.commit()

    return jsonify({'message': 'Trilha deleted successfully'}), 200


"""CRUD DE TRILHA E SEUS COMENTARIOS"""


def get_trilha_comentarios(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    comentarios = trilha.comentarios
    comentarios_data = [
        {'id': comentario.id,
         'descricao': comentario.descricao,
         'id_user': comentario.id_user
         } for comentario in comentarios
    ]
    return jsonify(comentarios=comentarios_data), 200


def create_trilha_comentario(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    descricao = request.json.get('descricao')

    id_user = get_jwt_identity()
    if not descricao:
        return jsonify({'message': 'Missing data descricao'}), 400

    novo_comentario = Comentario(descricao=descricao, id_user=id_user)
    trilha.comentarios.append(novo_comentario)

    try:
        db.session.add(novo_comentario)
        db.session.commit()

        comentario_data = {
            'id': novo_comentario.id,
            'descricao': novo_comentario.descricao,
            'id_user': novo_comentario.id_user
        }
        return jsonify(comentario=comentario_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to create comentario', 'error': str(e)}), 500


def delete_trilha_comentario(trilha_id, comentario_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    comentario = Comentario.query.get(comentario_id)
    if not comentario or comentario not in trilha.comentarios:
        return jsonify({'message': 'Comentario not found in this Trilha'}), 404

    try:
        trilha.comentarios.remove(comentario)
        db.session.commit()
        return jsonify({'message': 'Comentario deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to delete comentario', 'error': str(e)}), 500


"""CRUD DE TRILHA E SUAS AVALIACOES"""


def get_trilha_avaliacoes(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    avaliacoes = trilha.avaliacoes
    avaliacoes_data = [{'id': avaliacao.id, 'valor': avaliacao.valor, 'descricao': avaliacao.descricao, 'id_user': avaliacao.id_user} for avaliacao in avaliacoes]
    return jsonify(avaliacoes=avaliacoes_data), 200


def create_trilha_avaliacao(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    valor = request.json.get('valor')
    descricao = request.json.get('descricao')
    id_user = get_jwt_identity()

    if valor is None:
        return jsonify({'message': 'Missing data valor'}), 400

    nova_avaliacao = Avaliacao(valor=valor, descricao=descricao, id_user=id_user)
    trilha.avaliacoes.append(nova_avaliacao)

    try:
        db.session.add(nova_avaliacao)
        db.session.commit()

        avaliacao_data = {
            'id': nova_avaliacao.id,
            'valor': nova_avaliacao.valor,
            'descricao': nova_avaliacao.descricao,
            'id_user': nova_avaliacao.id_user
        }
        return jsonify(avaliacao=avaliacao_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to create avaliacao', 'error': str(e)}), 500


def delete_trilha_avaliacao(trilha_id, avaliacao_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    avaliacao = Avaliacao.query.get(avaliacao_id)
    if not avaliacao or avaliacao not in trilha.avaliacoes:
        return jsonify({'message': 'Avaliacao not found in this Trilha'}), 404

    try:
        trilha.avaliacoes.remove(avaliacao)
        db.session.delete(avaliacao)
        db.session.commit()
        return jsonify({'message': 'Avaliacao deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to delete avaliacao', 'error': str(e)}), 500


"""CRUD DE TRILHA E SEUS CURSOS"""


def create_trilha_curso(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    curso_id = request.json.get('curso_id')
    if not curso_id:
        return jsonify({'message': 'Missing curso_id'}), 400

    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    if curso in trilha.cursos_associados:
        return jsonify({'message': 'Curso already associated with this Trilha'}), 409

    trilha.cursos_associados.append(curso)

    try:
        db.session.commit()
        curso_data = {'id': curso.id, 'titulo': curso.titulo, 'descricao': curso.descricao}
        return jsonify(curso=curso_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to add Curso to Trilha', 'error': str(e)}), 500


def get_trilha_cursos(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    cursos = trilha.cursos_associados
    cursos_data = [{'id': curso.id, 'titulo': curso.titulo, 'descricao': curso.descricao} for curso in cursos]
    return jsonify(cursos=cursos_data), 200


def delete_trilha_curso(trilha_id, curso_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    curso = Curso.query.get(curso_id)
    if not curso or curso not in trilha.cursos_associados   :
        return jsonify({'message': 'Curso not found in this Trilha'}), 404

    try:
        trilha.cursos.remove(curso)
        db.session.commit()
        return jsonify({'message': 'Curso removed from Trilha successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to remove Curso from Trilha', 'error': str(e)}), 500


"""CRUD DE TRILHA E SUAS AULAS"""


def create_trilha_aula(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    aula_id = request.json.get('aula_id')
    if not aula_id:
        return jsonify({'message': 'Missing aula_id'}), 400

    aula = Aula.query.get(aula_id)
    if not aula:
        return jsonify({'message': 'Aula not found'}), 404

    if aula in trilha.aulas:
        return jsonify({'message': 'Aula already associated with this Trilha'}), 409

    trilha.aulas.append(aula)

    try:
        db.session.commit()
        aula_data = {'id': aula.id, 'titulo': aula.titulo, 'descricao': aula.descricao}
        return jsonify(aula=aula_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to add Aula to Trilha', 'error': str(e)}), 500


def get_trilha_aulas(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    aulas = trilha.aulas
    aulas_data = [{'id': aula.id, 'titulo': aula.titulo, 'descricao': aula.descricao} for aula in aulas]
    return jsonify(aulas=aulas_data), 200


def delete_trilha_aula(trilha_id, aula_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    aula = Aula.query.get(aula_id)
    if not aula or aula not in trilha.aulas:
        return jsonify({'message': 'Aula not found in this Trilha'}), 404

    try:
        trilha.aulas.remove(aula)
        db.session.commit()
        return jsonify({'message': 'Aula removed from Trilha successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to remove Aula from Trilha', 'error': str(e)}), 500


"""CRUD DE TRILHA E SEUS USUARIOS"""


def add_logged_in_user_to_trilha(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user in trilha.users:
        return jsonify({'message': 'User already enrolled in this Trilha'}), 409

    trilha.users.append(user)

    try:
        db.session.commit()
        user_data = {'id': user.id, 'username': user.username}
        return jsonify(user=user_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to add User to Trilha', 'error': str(e)}), 500


def get_trilha_users(trilha_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    users = trilha.users
    users_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(users=users_data), 200


def remove_user_from_trilha(trilha_id, user_id):
    trilha = Trilha.query.get(trilha_id)
    if not trilha:
        return jsonify({'message': 'Trilha not found'}), 404

    user = User.query.get(user_id)
    if not user or user not in trilha.users:
        return jsonify({'message': 'User not found in this Trilha'}), 404

    try:
        trilha.users.remove(user)
        db.session.commit()
        return jsonify({'message': 'User removed from Trilha successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to remove User from Trilha', 'error': str(e)}), 500
