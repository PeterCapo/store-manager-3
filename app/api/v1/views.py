from flask_restful import Resource
import json
from flask import jsonify, make_response, request
from app.api.v1.models.products import *
from app.api.v1.validators.utils import Validators
sales = []


class SpecificSale(Resource):
    def get(self, id):
        return make_response(jsonify(
            {
                'Status': "OK",
                'Message': "Success",
                'specific sale': sales[id]
            }), 200)


class SpecificProduct(Resource):
    def get(self, id):
        return make_response(jsonify(
            {
                'Status': "OK",
                'Message': "Success",
                'specific product': products[id]
            }), 200)


class DeleteProduct(Resource):
    def delete(self, id):
        product = products[id]
        if product:
            products.remove(product)
            return {'Message': "Deleted"},
        return {'Message': "Not found"}


class UpdateProduct(Resource):
    def put(self, id):
        data = json.loads(request.data)
        assert(data['Product Name'])
        assert(data['Category'])
        assert(data['Stock Balance'])
        assert(data['Minimum Inventory'])
        assert (data['Price'])
        assert (data['id'])

        for index, product in enumerate(products):
            if product['id'] == data['id']:
                new_product = {
                    "productName": data['Product Name'],
                    "category": data['Category'],
                    "stockBalance": data['Stock Balance'],
                    "minStockBalance": data['Minimum Inventory'],
                    "price": data['Price'],
                    "id": data['id']
                    }

                products[index] = new_product

                return make_response(jsonify(
                    {
                        'Message': 'Product updated',
                        'status': 'ok',
                        'Data': new_product
                    }), 200)


class Products(Resource):
    def get(self):
        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My Products': products
            }), 200)

    def post(self):
        data = request.get_json()
        id = len(products) + 1
        productName = data['Product Name']
        category = data['Category']
        stockBalance = data['Stock Balance']
        minStockBalance = data['Minimum Inventory']
        price = data['Price']

        if not Validators().valid_product_name(productName):
            return {'message': 'Enter a valid product name'}, 400

        payload = {
            'id': id,
            'Product Name': productName, 'Stock Balance': stockBalance,
            'Minimum Inventory': minStockBalance,
            'Category': category,
            'Price': price
        }
        products.append(payload)

        product = Product(
            productName, price,
            category, stockBalance,
            minStockBalance
            )
        product.save

        return make_response(jsonify(
            {
                'Message': 'Product created',
                'status': 'ok',
                'Data': products
            }), 201)


class Sales(Resource):
    def get(self):
        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My Sales': sales
            }), 200)

    def post(self):
        data = request.get_json()
        id = len(sales) + 1
        itemName = data['Item Name']
        attendant = data['Attendant']
        quantity = data['Quantity']
        price = data['Price']
        productId = data['product id']

        for product in products:
            if productId == int(product['id']):
                payload = {
                    'id': id,
                    'Item Name': itemName,
                    'Attendant': attendant,
                    'Quantity': quantity,
                    'Price': price,
                    'product id': productId
                    }
        sales.append(payload)
        product['Stock Balance'] -= 1

        return make_response(jsonify(
            {
                'Message': 'Sales created',
                'status': 'ok',
                'Data': sales
            }), 201)
