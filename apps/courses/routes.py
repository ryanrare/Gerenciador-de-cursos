from flask import jsonify
from . import courses_bp


@courses_bp.route('/')
def home():
    return jsonify(message="Courses API!")
