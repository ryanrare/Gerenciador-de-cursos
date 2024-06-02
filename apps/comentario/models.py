from apps.db import db


class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comentarios', lazy=True))
