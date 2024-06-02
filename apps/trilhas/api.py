from flask import jsonify, request
from .models import Trilha
from apps.comentario.models import Comentario
from apps.db import db


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

    return jsonify({'message': 'Trilha created successfully'}), 201


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
    id_user = request.json.get('id_user')

    if not descricao or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    novo_comentario = Comentario(descricao=descricao, id_user=id_user)
    trilha.comentarios.append(novo_comentario)

    try:
        db.session.add(novo_comentario)
        db.session.commit()
        return jsonify({'message': 'Comentario created successfully'}), 201
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
