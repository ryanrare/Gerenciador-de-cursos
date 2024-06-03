import pytest
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from apps import create_app
from apps.db import db
from apps.users.models import User


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
            new_user = User(username='testuser', email='testuser@example.com', password_hash=generate_password_hash('testpassword'))
            db.session.add(new_user)
            db.session.commit()
            user_id = new_user.id
        else:
            user_id = existing_user.id

        access_token = create_access_token(identity=user_id)
        return access_token


def test_user_endpoints(test_client, token):
    # Certifique-se de que o usuário "ALO" não existe antes de tentar registrá-lo
    with test_client.application.app_context():
        existing_user = User.query.filter_by(username='ALO').first()
        if existing_user:
            db.session.delete(existing_user)
            db.session.commit()

    # Test user registration (POST /users/register/)
    user_data = {
        "username": "ALO",
        "password": "new_password",
        "email": "alo@alo.com"
    }
    response = test_client.post('/users/register/', json=user_data)
    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data['data']['username'] == user_data['username']
    assert response_data['data']['email'] == user_data['email']

    # Test get all users (GET /users/)
    response = test_client.get('/users/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'users' in data

    # Get the ID of the newly created user for further testing
    new_user_id = None
    for user in data['users']:
        if user['username'] == 'ALO':
            new_user_id = user['id']
            break

    assert new_user_id is not None

    # Test get specific user (GET /users/{id}/)
    response = test_client.get(f'/users/{new_user_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['username'] == 'ALO'

    # Test update user (PUT /users/{id}/)
    update_data = {
        'username': 'updateduser',
        'email': 'updateduser@example.com'
    }
    response = test_client.put(f'/users/{new_user_id}/', json=update_data, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert response_data['data']['username'] == user_data['username']
    assert response_data['data']['email'] == user_data['email']

    # Test delete user (DELETE /users/{id}/)
    response = test_client.delete(f'/users/{new_user_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'User deleted successfully'

    # Test get specific user after deletion (should return 404)
    response = test_client.get(f'/users/{new_user_id}/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 404
