"""
A command-line utility that lets you interact with application in various ways.
"""

import unittest

from flask_migrate import MigrateCommand
from flask_script import Manager
import coverage

from app import create_app, db
from app.api.models.user import User

# coverage settings
COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'app/tests/*'
    ]
)
COV.start()

# create app
app = create_app()

# create manager instance
manager = Manager(app)

# add migration commands
manager.add_command('db', MigrateCommand)


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(
        username='username',
        email='test@email.com',
        password='test'
    ))
    db.session.add(User(
        username='username1',
        email='test1@email.com',
        password='test1'
    ))
    db.session.commit()


@manager.command
def test():
    """Runs the unit tests without code coverage."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
