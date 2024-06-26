from apps.db import db
from apps.utils.association_tables import trilha_curso, trilha_aula, trilha_user


trilha_comentario = db.Table('trilha_comentario',
    db.Column('trilha_id', db.Integer, db.ForeignKey('trilha.id'), primary_key=True),
    db.Column('comentario_id', db.Integer, db.ForeignKey('comentario.id'), primary_key=True)
)

trilha_avaliacao = db.Table('trilha_avaliacao',
    db.Column('trilha_id', db.Integer, db.ForeignKey('trilha.id'), primary_key=True),
    db.Column('avaliacao_id', db.Integer, db.ForeignKey('avaliacao.id'), primary_key=True)
)


class Trilha(db.Model):
    __tablename__ = 'trilha'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)

    cursos_associados = db.relationship('Curso', secondary=trilha_curso, lazy='subquery', backref=db.backref('trilhas', lazy=True))
    aulas = db.relationship('Aula', secondary=trilha_aula, lazy='subquery', backref=db.backref('trilhas', lazy=True))
    comentarios = db.relationship('Comentario', secondary=trilha_comentario, lazy='subquery', backref=db.backref('trilhas', lazy=True))
    users = db.relationship('User', secondary=trilha_user, lazy='subquery', backref=db.backref('trilhas', lazy=True))
    avaliacoes = db.relationship('Avaliacao', secondary='trilha_avaliacao', lazy='subquery', backref=db.backref('trilhas', lazy=True))
