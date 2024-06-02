from flask import Blueprint

aulas_bp = Blueprint('aulas', __name__)

from . import routes, models
