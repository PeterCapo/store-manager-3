import unittest
import json
from app import create_app


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.admin_data = {
            "email": "admin@gmail.com",
            "password": "admin"
        }
        self.invalid_data = {
            "email": "admin@",
            "password": "admin"
        }
        self.invalid_pass = {
            "email": "admin@gmail.com",
            "password": ""
        }

    def login(self):
        response = self.client.post(
            "api/v1/login",
            data=json.dumps(self.admin_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def get_token(self):
        response = self.login()
        token = json.loads(response.data).get("token", None)
        return token

    def test_login(self):
        response = self.client.post(
            "api/v1/login",
            data=json.dumps(self.admin_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        response = self.client.post(
            "api/v1/login",
            data=json.dumps(self.invalid_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 404)

    def test_invalid_password(self):
        response = self.client.post(
            "api/v1/login",
            data=json.dumps(self.invalid_pass),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 404)
