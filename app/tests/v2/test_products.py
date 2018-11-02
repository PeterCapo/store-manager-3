import unittest
import json
from app import create_app
from ...db_con import connection, create_tables


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            connection()
            create_tables()

        self.data = {
            "Product Name": "sony",
            "Category": "electronics",
            "Stock Balance": 600,
            "Price": 20000,
            "product_id":3
            }
        self.admin_data = {
            "email": "admin@gmail.com",
            "password": "admin",
            "admin": "True"
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
        """get token """
        response = self.login()
        token = json.loads(response.data).get("token", None)
        return token


    def test_delete_product(self):
        token = self.get_token()

        res = self.client.delete(
                '/api/v2/products/1',
                headers={"content-type": "application/json",
                         'Authorization': f'Bearer {token}'}
            )
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
