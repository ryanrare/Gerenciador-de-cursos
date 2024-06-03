from flask import jsonify, request
from .models import Curso
from apps.avaliacao.models import Avaliacao
from apps.aulas.models import Aula
from apps.comentario.models import Comentario
from apps.db import db


def get_all_cursos():
    cursos = Curso.query.all()
    cursos_data = [{'id': curso.id, 'titulo': curso.titulo, 'descricao': curso.descricao} for curso in cursos]
    return jsonify(cursos=cursos_data), 200


def create_curso(data):
    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo or not descricao:
        return jsonify({'message': 'Missing data'}), 400

    novo_curso = Curso(titulo=titulo, descricao=descricao)
    session = db.Session()
    session.add(novo_curso)
    session.commit()

    return jsonify({'message': 'Curso created successfully'}), 201


def get_curso(id):
    curso = Curso.query.get(id)
    if curso is None:
        return jsonify({'message': 'Curso not found'}), 404
    return jsonify({'id': curso.id, 'titulo': curso.titulo, 'descricao': curso.descricao}), 200


def update_curso(id, data):
    curso = Curso.query.get(id)
    if curso is None:
        return jsonify({'message': 'Curso not found'}), 404

    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo or not descricao:
        return jsonify({'message': 'Missing data'}), 400

    curso.titulo = titulo
    curso.descricao = descricao
    session = db.Session()
    session.commit()

    return jsonify({'message': 'Curso updated successfully'}), 200


def delete_curso(id):
    curso = Curso.query.get(id)
    if curso is None:
        return jsonify({'message': 'Curso not found'}), 404

    session = db.Session()
    session.delete(curso)
    session.commit()

    return jsonify({'message': 'Curso deleted successfully'}), 200


"""CRUD DE CURSO E SEUS COMENTARIOS"""


def get_curso_comentarios(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    comentarios = curso.comentarios
    comentarios_data = [
        {
            'id': comentario.id,
            'descricao': comentario.descricao,
            'id_user': comentario.id_user
        } for comentario in comentarios
    ]
    return jsonify(comentarios=comentarios_data), 200


def create_curso_comentario(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    descricao = request.json.get('descricao')
    id_user = request.json.get('id_user')

    if not descricao or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    novo_comentario = Comentario(descricao=descricao, id_user=id_user)
    curso.comentarios.append(novo_comentario)

    try:
        db.session.add(novo_comentario)
        db.session.commit()
        return jsonify({'message': 'Comentario created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to create comentario', 'error': str(e)}), 500


def delete_curso_comentario(curso_id, comentario_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    comentario = Comentario.query.get(comentario_id)
    if not comentario or comentario not in curso.comentarios:
        return jsonify({'message': 'Comentario not found in this Curso'}), 404

    try:
        curso.comentarios.remove(comentario)
        db.session.commit()
        return jsonify({'message': 'Comentario deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to delete comentario', 'error': str(e)}), 500


"""CRUD DE CURSO E SUAS AVALIACOES"""


def create_curso_avaliacao(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    valor = request.json.get('valor')
    descricao = request.json.get('descricao')
    id_user = request.json.get('id_user')

    if valor is None or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    nova_avaliacao = Avaliacao(valor=valor, descricao=descricao, id_user=id_user)
    curso.avaliacoes.append(nova_avaliacao)

    try:
        db.session.add(nova_avaliacao)
        db.session.commit()
        return jsonify({'message': 'Avaliacao created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to create avaliacao', 'error': str(e)}), 500


def get_curso_avaliacoes(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    avaliacoes = curso.avaliacoes
    avaliacoes_data = [
        {
            'id': avaliacao.id,
            'valor': avaliacao.valor,
            'descricao': avaliacao.descricao,
            'id_user': avaliacao.id_user
        } for avaliacao in avaliacoes
    ]
    return jsonify(avaliacoes=avaliacoes_data), 200


def delete_curso_avaliacao(curso_id, avaliacao_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    avaliacao = Avaliacao.query.get(avaliacao_id)
    if not avaliacao or avaliacao not in curso.avaliacoes:
        return jsonify({'message': 'Avaliacao not found in this Curso'}), 404

    try:
        curso.avaliacoes.remove(avaliacao)
        db.session.commit()
        return jsonify({'message': 'Avaliacao deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to delete avaliacao', 'error': str(e)}), 500


"""CRUD DE CURSO E SUAS AULAS"""


def get_curso_aulas(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    aulas = curso.aulas
    aulas_data = [
        {
            'id': aula.id,
            'titulo': aula.titulo,
            'descricao': aula.descricao
        } for aula in aulas
    ]
    return jsonify(aulas=aulas_data), 200


def create_curso_aula(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')

    if not titulo:
        return jsonify({'message': 'Missing data'}), 400

    nova_aula = Aula(titulo=titulo, descricao=descricao)
    curso.aulas.append(nova_aula)

    try:
        db.session.add(nova_aula)
        db.session.commit()
        return jsonify({'message': 'Aula created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to create aula', 'error': str(e)}), 500


def delete_curso_aula(curso_id, aula_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return jsonify({'message': 'Curso not found'}), 404

    aula = Aula.query.get(aula_id)
    if not aula or aula not in curso.aulas:
        return jsonify({'message': 'Aula not found in this Curso'}), 404

    try:
        curso.aulas.remove(aula)
        db.session.commit()
        return jsonify({'message': 'Aula deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Unable to delete aula', 'error': str(e)}), 500
