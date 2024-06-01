import pytest
from flask import Flask
from config import TestingConfig
from apps import create_app, db


@pytest.fixture(scope='function')
def client(app):
    return app.test_client()


@pytest.fixture(scope='function')
def _db(app):
    db.app = app
    return db


@pytest.fixture(scope='function')
def session(_db):
    connection = _db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    with flask_app.app_context():
        db.create_all()
        testing_client = flask_app.test_client()

        yield testing_client

        db.drop_all()
