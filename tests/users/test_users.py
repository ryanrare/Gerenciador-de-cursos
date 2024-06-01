# -*- coding: utf-8 -*-

from werkzeug.security import check_password_hash
from apps.users.models import User


def test_index_response_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_post_user(test_client):
    # Dados de teste
    user_data = {
        'name': 'testuser',
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = test_client.post('/users/register/', json=user_data)

    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data['data']['username'] == user_data['username']

    user = User.query.filter_by(username=user_data['username']).first()
    assert user is not None
    assert user.username == user_data['username']
    assert check_password_hash(user.password_hash, user_data['password'])
