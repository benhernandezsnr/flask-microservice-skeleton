import flask
from app.app_factory import AppFactory
from app.models import db
from flask.ext.testing import TestCase
import json


class ApiTestCase(TestCase):
    def create_app(self):
        app = flask.Flask(__name__)
        app.environment = 'test'
        AppFactory.setup(app)
        return app
        
    def setUp(self):
        self.test_app = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        return super(TestCase, self).tearDown()

    def post_json(self, url, data=None):
        return self.test_app.post(url, data=json.dumps(data), content_type='application/json')

    def assertApiJsonResultEquals(self, response, status_code=200, result=None):
        data = json.loads(response.data)
        result = data['result']
        self.assertEquals(status_code, response.status_code)
        self.assertEquals(result, result)