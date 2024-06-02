from flask import Blueprint

avaliacao_bp = Blueprint('avaliacao', __name__)

from . import routes, models
