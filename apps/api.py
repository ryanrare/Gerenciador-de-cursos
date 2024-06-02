# -*- coding: utf-8 -*-

from flask_restful import Api, Resource
from apps.users import users_bp
from apps.courses import courses_bp
from apps.trilhas import trilhas_bp
from apps.aulas import aulas_bp
from apps.comentario import comentario_bp
from apps.avaliacao import avaliacao_bp


class Index(Resource):
    @staticmethod
    def get():
        return {'hello': 'world'}


api = Api()


def configure_api(app):
    api.add_resource(Index, '/')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(courses_bp, url_prefix='/courses')
    app.register_blueprint(trilhas_bp, url_prefix='/trilhas')
    app.register_blueprint(aulas_bp, url_prefix='/aulas')
    app.register_blueprint(comentario_bp, url_prefix='/comentarios')
    app.register_blueprint(avaliacao_bp, url_prefix='/avaliacoes')
    api.init_app(app)
