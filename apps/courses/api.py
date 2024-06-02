from flask import jsonify, request
from .models import Curso
from apps import db


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
