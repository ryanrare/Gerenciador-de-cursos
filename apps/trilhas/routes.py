from flask import jsonify
from . import trilhas_bp


@trilhas_bp.route('/')
def home():
    return jsonify(message="Trilhas API!")
