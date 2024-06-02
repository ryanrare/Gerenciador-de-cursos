import pytest
from flask_jwt_extended import create_access_token

from apps.trilhas.models import Trilha
from apps.users.models import User
from apps import create_app
from apps.db import db


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with flask_app.app_context():
        db.create_all()
        yield flask_app.test_client()
        db.drop_all()


@pytest.fixture(scope='module')
def token(test_client):
    with test_client.application.app_context():
        existing_user = User.query.filter_by(username='testuser').first()
        if not existing_user:
            user = User(username='testuser', email='testuser@example.com', password_hash='testpassword')
            db.session.add(user)
            db.session.commit()

        access_token = create_access_token(identity=user.id)
        return access_token



def test_get_all_trilhas(test_client, token):
    trilha1 = Trilha(titulo='Trilha 1', descricao='Descrição da trilha 1')
    trilha2 = Trilha(titulo='Trilha 2', descricao='Descrição da trilha 2')
    db.session.add_all([trilha1, trilha2])
    db.session.commit()

    response = test_client.get('/trilhas/', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200

    data = response.get_json()
    assert len(data['trilhas']) == 2
    assert data['trilhas'][0]['titulo'] == 'Trilha 1'
    assert data['trilhas'][1]['titulo'] == 'Trilha 2'


def test_create_trilha(test_client, token):
    trilha_data = {
        'titulo': 'Nova Trilha',
        'descricao': 'Descrição da nova trilha'
    }

    response = test_client.post('/trilhas/', json=trilha_data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201

    data = response.get_json()
    assert data['message'] == 'Trilha created successfully'

    with test_client.application.app_context():
        trilha = Trilha.query.filter_by(titulo='Nova Trilha').first()
        assert trilha is not None
        assert trilha.descricao == 'Descrição da nova trilha'


def test_update_trilha(test_client, token):
    with test_client.application.app_context():
        trilha = Trilha(titulo='Trilha para atualizar', descricao='Descrição da trilha para atualizar')
        db.session.add(trilha)
        db.session.commit()

        update_data = {
            'titulo': 'Trilha atualizada',
            'descricao': 'Descrição atualizada da trilha'
        }

        with db.session.begin():
            response = test_client.put(f'/trilhas/{trilha.id}/', json=update_data, headers={'Authorization': f'Bearer {token}'})

        assert response.status_code == 200

        with test_client.application.app_context():
            trilha_atualizada = Trilha.query.get(trilha.id)
            assert trilha_atualizada is not None
            assert trilha_atualizada.titulo == 'Trilha atualizada'
            assert trilha_atualizada.descricao == 'Descrição atualizada da trilha'


def test_delete_trilha(test_client, token):
    with test_client.application.app_context():
        trilha = Trilha(titulo='Trilha para excluir', descricao='Descrição da trilha para excluir')
        db.session.add(trilha)
        db.session.commit()

        with db.session.begin():
            response = test_client.delete(f'/trilhas/{trilha.id}/', headers={'Authorization': f'Bearer {token}'})

        assert response.status_code == 200

        with test_client.application.app_context():
            trilha_excluida = Trilha.query.get(trilha.id)
            assert trilha_excluida is None
