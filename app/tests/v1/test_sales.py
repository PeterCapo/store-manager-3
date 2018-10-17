import unittest
import json
from ... import create_app


class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {}

    def test_create_sales(self):
        sale_data = {
            "Item Name": "Infinix",
            "Attendant": "James",
            "Quantity": 2,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/sales',
            data=json.dumps(sale_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['Message'], "Sales created")

    def test_invalid_item_name(self):
        sale_data = {
            "Item Name": "",
            "Attendant": "James",
            "Quantity": 2,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/sales',
            data=json.dumps(sale_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertTrue(response_data['Message'], "Enter valid item name")

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


if __name__ == '__main__':
    unittest.main()
