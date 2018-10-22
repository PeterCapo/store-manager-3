import unittest
import json
from ... import create_app


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {}

    def test_create_products(self):
        products_data = {
            "Product Name": "Infinix",
            "Category": "Electronics",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/products',
            data=json.dumps(products_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['Message'], "Product created")
    
    def test_update_products(self):
        new_product = {
            "Product Name": "samsung",
            "Category": "Electronics",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000,
            "id": 1
            }
        res = self.client.put(
            '/api/v1/products/1',
            data=json.dumps(new_product),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['Message'], "Product updated")   

    def test_invalid_product_name(self):
        products_data = {
            "Product Name": "",
            "Category": "Electronics",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/products',
            data=json.dumps(products_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertTrue(response_data['Message'], "Enter valid product name")

    def test_invalid_product_category(self):
        products_data = {
            "Product Name": "LG prada",
            "Category": "",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/products',
            data=json.dumps(products_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertTrue(response_data['Message'], "Enter valid product name")

    def test_get_all_products(self):

        res = self.client.get(
            '/api/v1/products',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_specific_product(self):

        res = self.client.get(
            '/api/v1/products/1',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)
    
    def test_delete_product(self):
        response = self.client.delete(
            '/api/v1/products/0',
            headers={"content-type": "application/json"}
            )

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
