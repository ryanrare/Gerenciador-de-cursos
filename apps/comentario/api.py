from flask import jsonify
from .models import Comentario
from apps import db


def get_all_comentarios():
    comentarios = Comentario.query.all()
    comentarios_data = [
        {'id': comentario.id,
         'descricao': comentario.descricao,
         'id_user': comentario.id_user
         } for comentario in comentarios
    ]
    return jsonify(comentarios=comentarios_data), 200


def create_comentario(data):
    descricao = data.get('descricao')
    id_user = data.get('id_user')

    if not descricao or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    novo_comentario = Comentario(descricao=descricao, id_user=id_user)
    session = db.Session()
    session.add(novo_comentario)
    session.commit()

    return jsonify({'message': 'Comentario created successfully'}), 201


def get_comentario(id):
    comentario = Comentario.query.get(id)
    if comentario is None:
        return jsonify({'message': 'Comentario not found'}), 404
    return jsonify({'id': comentario.id, 'descricao': comentario.descricao, 'id_user': comentario.id_user}), 200


def update_comentario(id, data):
    comentario = Comentario.query.get(id)
    if comentario is None:
        return jsonify({'message': 'Comentario not found'}), 404

    descricao = data.get('descricao')
    id_user = data.get('id_user')

    if not descricao or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    comentario.descricao = descricao
    comentario.id_user = id_user
    session = db.Session()
    session.commit()

    return jsonify({'message': 'Comentario updated successfully'}), 200


def delete_comentario(id):
    comentario = Comentario.query.get(id)
    if comentario is None:
        return jsonify({'message': 'Comentario not found'}), 404

    session = db.Session()
    session.delete(comentario)
    session.commit()

    return jsonify({'message': 'Comentario deleted successfully'}), 200
