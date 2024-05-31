# tests/users/test_user_model.py
import unittest
from apps import create_app
from apps.db import db
from apps.users.models import User


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        user = User(username='testuser', email='test@example.com', password_hash='hashed_password')
        db.session.add(user)
        db.session.commit()

        found_user = User.query.filter_by(username='testuser').first()

        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.email, 'test@example.com')


if __name__ == '__main__':
    unittest.main()
