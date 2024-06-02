import pytest
from flask_jwt_extended import create_access_token
from apps import create_app
from apps.db import db
from apps.users.models import User
from werkzeug.security import check_password_hash


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
def new_user():
    return User(username='testuser', email='testuser@example.com', password_hash='testpassword')


@pytest.fixture(scope='module')
def add_user_to_db(test_client, new_user):
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()
    yield
    with test_client.application.app_context():
        db.session.delete(new_user)
        db.session.commit()


@pytest.fixture(scope='module')
def token(test_client, new_user, add_user_to_db):
    with test_client.application.app_context():
        access_token = create_access_token(identity=new_user.id)
        return access_token


def test_index_response_200(test_client, token):
    response = test_client.get('/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200


def test_post_user(test_client):
    user_data = {
        "username": "rsssddddssyaan",
        "password": "senhadonovousuario",
        "email": "ryasssssn@asssssaaa.com"
    }

    response = test_client.post('/users/register/', json=user_data)
    assert response.status_code == 201

    response_data = response.get_json()
    assert response_data['data']['username'] == user_data['username']

    with test_client.application.app_context():
        user = User.query.filter_by(username=user_data['username']).first()
        assert user is not None
        assert user.username == user_data['username']


def test_get_users(test_client, token):
    response = test_client.get('/users/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'users' in data


def test_get_user(test_client, token, new_user):
    response = test_client.get(f'/users/{new_user.id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['username'] == 'testuser'


def test_update_user(test_client, token, new_user):
    update_data = {
        'username': 'updateduser',
        'email': 'updateduser@example.com'
    }
    response = test_client.put(f'/users/{new_user.id}/', json=update_data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200

    data = response.get_json()
    assert data['username'] == 'updateduser'


def test_delete_user(test_client, token, new_user):
    response = test_client.delete(f'/users/{new_user.id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'User deleted'

    with test_client.application.app_context():
        user = User.query.get(new_user.id)
        assert user is None
