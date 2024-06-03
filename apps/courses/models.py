from apps.db import db
from apps.utils.association_tables import curso_user, curso_aula


curso_avaliacao = db.Table('curso_avaliacao',
                           db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key=True),
                           db.Column('avaliacao_id', db.Integer, db.ForeignKey('avaliacao.id'), primary_key=True)
                           )

curso_comentario = db.Table('curso_comentario',
                            db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key=True),
                            db.Column('comentario_id', db.Integer, db.ForeignKey('comentario.id'), primary_key=True)
                            )


class Curso(db.Model):

    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)

    users = db.relationship('User', secondary=curso_user, lazy='subquery', backref=db.backref('courses', lazy=True))
    aulas = db.relationship('Aula', secondary=curso_aula, lazy='subquery', backref=db.backref('courses', lazy=True))
    avaliacoes = db.relationship('Avaliacao', secondary=curso_avaliacao, lazy='subquery',
                                 backref=db.backref('courses', lazy=True))
    comentarios = db.relationship('Comentario', secondary=curso_comentario, lazy='subquery',
                                  backref=db.backref('courses', lazy=True))
    from apps.utils.association_tables import trilha_curso
    trilhas_associadas = db.relationship('Trilha', secondary=trilha_curso, lazy='subquery',
                                         backref=db.backref('courses', lazy=True))
