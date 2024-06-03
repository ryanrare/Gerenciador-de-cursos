from datetime import datetime
from apps.db import db, ma
from werkzeug.security import generate_password_hash, check_password_hash
from apps.comentario.models import Comentario
from apps.avaliacao.models import Avaliacao
from apps.utils.association_tables import trilha_user


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)

    comentarios = db.relationship('Comentario', backref='comentario_user', lazy=True)
    avaliacoes = db.relationship('Avaliacao', backref='avaliacoes_user', lazy=True)

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)
