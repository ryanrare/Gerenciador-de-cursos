from apps.db import db


class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('avaliacoes', lazy=True))
