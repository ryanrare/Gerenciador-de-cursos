from apps.db import db

trilha_curso = db.Table('trilha_curso',
    db.Column('trilha_id', db.Integer, db.ForeignKey('trilha.id'), primary_key=True),
    db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key=True)
)
