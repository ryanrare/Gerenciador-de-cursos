from flask import jsonify, request
from .models import Aula
from apps import db


def get_all_aulas():
    aulas = Aula.query.all()
    aulas_data = [{'id': aula.id, 'titulo': aula.titulo, 'descricao': aula.descricao} for aula in aulas]
    return jsonify(aulas=aulas_data), 200


def create_aula(data):
    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo or not descricao:
        return jsonify({'message': 'Missing data'}), 400

    nova_aula = Aula(titulo=titulo, descricao=descricao)
    session = db.Session()
    session.add(nova_aula)
    session.commit()

    return jsonify({'message': 'Aula created successfully'}), 201


def get_aula(id):
    aula = Aula.query.get(id)
    if aula is None:
        return jsonify({'message': 'Aula not found'}), 404
    return jsonify({'id': aula.id, 'titulo': aula.titulo, 'descricao': aula.descricao}), 200


def update_aula(id, data):
    aula = Aula.query.get(id)
    if aula is None:
        return jsonify({'message': 'Aula not found'}), 404

    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo or not descricao:
        return jsonify({'message': 'Missing data'}), 400

    aula.titulo = titulo
    aula.descricao = descricao
    session = db.Session()
    session.commit()

    return jsonify({'message': 'Aula updated successfully'}), 200


def delete_aula(id):
    aula = Aula.query.get(id)
    if aula is None:
        return jsonify({'message': 'Aula not found'}), 404

    session = db.Session()
    session.delete(aula)
    session.commit()

    return jsonify({'message': 'Aula deleted successfully'}), 200
