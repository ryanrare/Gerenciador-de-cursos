from flask import Blueprint

trilhas_bp = Blueprint('trilhas', __name__)

from . import routes
