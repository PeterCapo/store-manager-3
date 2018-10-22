from flask_restful import Resource
import json
from flask import Flask, jsonify, make_response, request
from flask_jwt import JWT, jwt_required, current_identity

sales = []
products = []


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

class UpdateProduct(Resource):           
    def put(self, id): 
        data = json.loads(request.data)
        assert( data['Product Name'])
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

                return new_product, 200

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

        payload = {
            'id': id,
            'Description': {
                'Product Name': productName, 'Stock Balance': stockBalance,
                'Minimum Inventory': minStockBalance,
                'Category': category
                },
            'Price': price
        }
        products.append(payload)

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

    @jwt_required
    def post(self):
        data = request.get_json()
        id = len(sales) + 1
        itemName = data['Item Name']
        attendant = data['Attendant']
        quantity = data['Quantity']
        price = data['Price']

        payload = {
            'id': id,
            'Item Name': itemName,
            'Attendant': attendant,
            'Quantity': quantity,
            'Price': price
        }
        sales.append(payload)

        return make_response(jsonify(
            {
                'Message': 'Sales created',
                'status': 'ok',
                'Data': sales
            }), 201)
