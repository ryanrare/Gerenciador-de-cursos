from flask import jsonify
from . import comentario_bp


@comentario_bp.route('/')
def home():
    return jsonify(message="Comentario API!")
