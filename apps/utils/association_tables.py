from apps.db import db

curso_user = db.Table('curso_user',
    db.Column('curso_id', db.Integer, db.ForeignKey('cursos.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

curso_aula = db.Table('curso_aula',
                      db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key=True),
                      db.Column('aula_id', db.Integer, db.ForeignKey('aula.id'), primary_key=True)
                      )

trilha_user = db.Table('trilha_user',
    db.Column('trilha_id', db.Integer, db.ForeignKey('trilha.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

trilha_curso = db.Table('trilha_curso',
    db.Column('trilha_id', db.Integer, db.ForeignKey('trilha.id'), primary_key=True),
    db.Column('curso_id', db.Integer, db.ForeignKey('curso.id'), primary_key=True)
)

trilha_aula = db.Table('trilha_aula',
    db.Column('trilha_id', db.Integer, db.ForeignKey('trilha.id'), primary_key=True),
    db.Column('aula_id', db.Integer, db.ForeignKey('aula.id'), primary_key=True)
)


