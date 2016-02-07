from tests.api import ApiTestCase
import json


class HealthTestCase(ApiTestCase):
    def test_ping(self):
        response = self.test_app.get('/health/ping')

        data = json.loads(response.data)
        self.assertEquals(data['status'], 'success')
        self.assertEquals(response.status_code, 200)
