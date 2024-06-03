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
        new_user = None
        if not existing_user:
            new_user = User(username='testuser', email='testuser@example.com', password_hash='testpassword')
            db.session.add(new_user)
            db.session.commit()

        access_token = None
        if new_user:
            access_token = create_access_token(identity=new_user.id)
            return access_token
        access_token = create_access_token(identity=existing_user.id)
        return access_token


def test_trilha_endpoints(test_client, token):
    # Test create_trilha endpoint
    data = {'titulo': 'Nova Trilha', 'descricao': 'Descrição da nova trilha'}
    response = test_client.post('/trilhas/', json=data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data['titulo'] == data['titulo']
    assert response_data['descricao'] == data['descricao']

    # Test get_trilha endpoint
    trilha_id = response_data['id']
    response = test_client.get(f'/trilhas/{trilha_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['id'] == trilha_id
    assert response_data['titulo'] == data['titulo']
    assert response_data['descricao'] == data['descricao']

    # Test update_trilha endpoint
    update_data = {'titulo': 'Trilha atualizada', 'descricao': 'Descrição atualizada da trilha'}
    response = test_client.put(f'/trilhas/{trilha_id}/', json=update_data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['message'] == 'Trilha updated successfully'

    # Test get_trilha endpoint after update
    response = test_client.get(f'/trilhas/{trilha_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['id'] == trilha_id
    assert response_data['titulo'] == update_data['titulo']
    assert response_data['descricao'] == update_data['descricao']

    # Test delete_trilha endpoint
    response = test_client.delete(f'/trilhas/{trilha_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['message'] == 'Trilha deleted successfully'

    # Test get_trilha endpoint after delete
    response = test_client.get(f'/trilhas/{trilha_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 404

