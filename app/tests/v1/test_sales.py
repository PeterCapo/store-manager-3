import unittest
import json
from ... import create_app


class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.admin_data = {
            "email": "admin@gmail.com",
            "password": "admin"
        }
        self.data = {
            "Attendant": "James",
            "Quantity": 2,
            "product id": 1,
        }

    def login(self):
        """ method to login admin """
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

    def test_get_all_sales(self):
        res = self.client.get(
            '/api/v1/sales',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_specific_sale(self):

        res = self.client.get(
            '/api/v1/sales/1',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_delete_product(self):
        token = self.get_token()

        res = self.client.delete(
            '/api/v1/sales/1',
            headers={"content-type": "application/json",
                     'Authorization': f'Bearer {token}'}
        )
        self.assertEqual(res.status_code, 200)

    def test_invalid_attendant_name(self):
        sales_data = {
            "Attendant": "",
            "Quantity": 2,
            "product id": 1,
        }
        res = self.client.post(
            '/api/v1/sales',
            data=json.dumps(sales_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertTrue(response_data['message'], "blank field not allowed")


if __name__ == '__main__':
    unittest.main()
