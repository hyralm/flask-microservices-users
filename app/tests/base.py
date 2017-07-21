"""BaseTest module"""

from flask_testing import TestCase

from app import db, create_app


app = create_app()


class BaseTestCase(TestCase):
    """Base Test class"""

    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
