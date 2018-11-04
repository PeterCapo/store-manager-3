import unittest
import json
from app import create_app
from ...db_con import connection, create_tables


class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            connection()
            create_tables()

        self.admin_data = {
            "email": "admin@gmail.com",
            "password": "admin",
            "admin": "True"
        }
        self.data = {
            "Attendant": "James",
            "Quantity": 2,
            "product id": 1,
        }

    def login(self):
        """ method to login admin """
        response = self.client.post(
            "api/v2/login",
            data=json.dumps(self.admin_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def get_token(self):
        response = self.login()
        token = json.loads(response.data).get("token", None)
        return token

    def test_get_all_sales(self):
        res = self.client.get(
            '/api/v2/sales',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_specific_sale(self):

        res = self.client.get(
            '/api/v2/sales/1',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
