from flask import jsonify
from .models import Avaliacao
from apps import db


def get_all_avaliacoes():
    avaliacoes = Avaliacao.query.all()
    avaliacoes_data = [
        {
            'id': avaliacao.id,
            'valor': avaliacao.valor,
            'descricao': avaliacao.descricao,
            'id_user': avaliacao.id_user
        } for avaliacao in avaliacoes
    ]
    return jsonify(avaliacoes=avaliacoes_data), 200


def create_avaliacao(data):
    valor = data.get('valor')
    descricao = data.get('descricao')
    id_user = data.get('id_user')

    if not valor or not descricao or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    nova_avaliacao = Avaliacao(valor=valor, descricao=descricao, id_user=id_user)
    session = db.Session()
    session.add(nova_avaliacao)
    session.commit()

    return jsonify({'message': 'Avaliacao created successfully'}), 201


def get_avaliacao(id):
    avaliacao = Avaliacao.query.get(id)
    if avaliacao is None:
        return jsonify({'message': 'Avaliacao not found'}), 404
    return jsonify({'id': avaliacao.id, 'valor': avaliacao.valor, 'descricao': avaliacao.descricao,
                    'id_user': avaliacao.id_user}), 200


def update_avaliacao(id, data):
    avaliacao = Avaliacao.query.get(id)
    if avaliacao is None:
        return jsonify({'message': 'Avaliacao not found'}), 404

    valor = data.get('valor')
    descricao = data.get('descricao')
    id_user = data.get('id_user')

    if not valor or not descricao or not id_user:
        return jsonify({'message': 'Missing data'}), 400

    avaliacao.valor = valor
    avaliacao.descricao = descricao
    avaliacao.id_user = id_user
    session = db.Session()
    session.commit()

    return jsonify({'message': 'Avaliacao updated successfully'}), 200


def delete_avaliacao(id):
    avaliacao = Avaliacao.query.get(id)
    if avaliacao is None:
        return jsonify({'message': 'Avaliacao not found'}), 404

    session = db.Session()
    session.delete(avaliacao)
    session.commit()

    return jsonify({'message': 'Avaliacao deleted successfully'}), 200
