from tests.api import ApiTestCase
import json


class HealthTestCase(ApiTestCase):
    def test_get_skeletons_trivial(self):
        response = self.test_app.get('/v1/skeleton')
        self.assertApiJsonResultEquals(response, result=[], status_code=200)

    def test_get_skeletons_trivial(self):
        response = self.post_json('/v1/skeleton', {'name': 'Harry'})
        self.assertApiJsonResultEquals(response, result={"id": 1, "name": "Harry"}, status_code=200)
