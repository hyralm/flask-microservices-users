"""Test Utils"""

import datetime

from app import db
from app.api.models.user import User


def add_user(username, email, password, created_at=datetime.datetime.utcnow()):
    """Add new user to the db."""
    user = User(
        username=username,
        email=email,
        password=password,
        created_at=created_at)
    db.session.add(user)
    db.session.commit()

    return user
