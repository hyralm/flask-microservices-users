"""Tests for the User Model."""

from sqlalchemy.exc import IntegrityError

from app import db
from app.api.models.user import User
from app.tests.base import BaseTestCase
from app.tests.utils import add_user


class TestUserModel(BaseTestCase):
    """Tests for the User Model."""

    def test_add_user(self):
        """Ensure the user is saved correct."""
        user = add_user('justatest', 'test@test.com', 'test')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)
        self.assertTrue(user.created_at)

    def test_add_user_duplicate_username(self):
        """Ensure the error is thrown if the username already exists."""
        add_user('justatest', 'test@test.com', 'test')
        duplicate_user = User(
            username='justatest',
            email='test@test2.com',
            password='test'
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        """Ensure the error is thrown if the email already exists."""
        add_user('justatest', 'test@test.com', 'test')
        duplicate_user = User(
            username='justanothertest',
            email='test@test.com',
            password='test'
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_passwords_are_random(self):
        """Ensure the passwords are random."""
        user_one = add_user('justatest', 'test@test.com', 'test')
        user_two = add_user('justatest2', 'test@test2.com', 'test')
        self.assertNotEqual(user_one.password, user_two.password)

    def test_encode_auth_token(self):
        """Ensure the method encode_auth_token behaves correctly."""
        user = add_user('justatest', 'test@test.com', 'test')
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        """Ensure the method decode_auth_token behaves correctly."""
        user = add_user('justatest', 'test@test.com', 'test')
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token), user.id)
