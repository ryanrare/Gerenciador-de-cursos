from flask import Blueprint

comentario_bp = Blueprint('comentario', __name__)

from . import routes, models
