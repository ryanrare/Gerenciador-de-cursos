from flask import jsonify
from . import avaliacao_bp


@avaliacao_bp.route('/')
def home():
    return jsonify(message="Avaliacao API!")
