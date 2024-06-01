# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
Session = sessionmaker()


def init_db(app):
    db.init_app(app)
    with app.app_context():
        Session.configure(bind=db.engine)
