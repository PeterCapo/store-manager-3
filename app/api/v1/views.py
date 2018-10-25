from flask_restful import Resource, reqparse
import json
import datetime
from flask import jsonify, make_response, request
from functools import wraps
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v1.models.products import products, Product
from app.api.v1.models.sales import sales, Sale
from app.api.v1.models.user import Users, User
from app.api.v1.validators.utils import Validators

user = User("admin@gmail.com", "admin", admin=True)
Users.append(user)


def admin_only(_f):
    ''' Restrict access if not admin '''
    @wraps(_f)
    def wrapper_function(*args, **kwargs):
        user = User().get_by_email(get_jwt_identity())

        print(user)

        if not user.admin:
            return {
                'message':
                'No access, you must be an admin to access'
                }, 401
        return _f(*args, **kwargs)
    return wrapper_function


def user_only(_f):
    ''' Restrict access if not attendant '''
    @wraps(_f)
    def wrapper_function(*args, **kwargs):
        user = User().get_by_email(get_jwt_identity())

        if user.admin:
            return {
                'message':
                'Anauthorized access, you must be an attendant to access'}, 401
        return _f(*args, **kwargs)
    return wrapper_function


class SpecificSale(Resource):
    def get(self, id):
        for sale in sales:
            if id == sale['id']:
                return make_response(jsonify(
                    {
                        'Message': 'Specific sale',
                        'status': 'ok',
                        'Data': sale
                    }), 200)

    @jwt_required
    @admin_only
    def delete(self, id):
        for sale in sales:
            if id == sale['id']:
                sales.remove(sale)
            return make_response(jsonify(
                {
                    'Message': 'Deleted',
                    'status': 'ok',
                }), 200)
        return{'Message': "Not Found"}


class SpecificProduct(Resource):
    def get(self, id):
        for product in products:
            if id == product['id']:
                return make_response(jsonify(
                    {
                        'Message': 'Specific product',
                        'status': 'ok',
                        'Data': product
                    }), 200)

    @jwt_required
    @admin_only
    def delete(self, id):
        for product in products:
            if id == product['id']:
                products.remove(product)
            return make_response(jsonify(
                {
                    'Message': 'Deleted',
                    'status': 'ok',
                }), 200)
        return{'Message': "Not Found"}


class UpdateProduct(Resource):
    @jwt_required
    @admin_only
    def put(self, id):
        data = json.loads(request.data)
        assert(data['Product Name'])
        assert(data['Category'])
        assert(data['Stock Balance'])
        assert (data['Price'])
        assert (data['id'])

        for index, product in enumerate(products):
            if product['id'] == data['id']:
                new_product = {
                    "productName": data['Product Name'],
                    "category": data['Category'],
                    "stockBalance": data['Stock Balance'],
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
    parser = reqparse.RequestParser()

    parser.add_argument("Product Name", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("Category", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("Stock Balance", type=int, required=True,
                        help="This field can not be left bank")
    parser.add_argument("Price", type=int, required=True,
                        help="This field can not be left bank")

    def get(self):
        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My Products': products
            }), 200)

    @jwt_required
    @admin_only
    def post(self):
        data = Products.parser.parse_args()
        id = len(products) + 1
        productName = data['Product Name']
        category = data['Category']
        stockBalance = data['Stock Balance']
        price = data['Price']

        if Validators.empty_fields(
                    self, productName, price, stockBalance, category
                        ):
                return {'message':
                        "blank field not allowed"}

        if next(
            filter(
                lambda x:
                x['Product Name'] == productName, products), None) is not None:
            return {'message':
                    "A product with name'{}' already exists."
                    .format(productName)
                    }

        payload = {
            'id': id,
            'Product Name': productName, 'Stock Balance': stockBalance,
            'Category': category,
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
    parser = reqparse.RequestParser()

    parser.add_argument("Attendant", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("Quantity", type=int, required=True,
                        help="This field can not be left bank")
    parser.add_argument("product id", type=int, required=True,
                        help="This field can not be left bank")

    def get(self):
        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My Sales': sales
            }), 200)

    @jwt_required
    @user_only
    def post(self):
        data = Sales.parser.parse_args()
        id = len(sales) + 1
        attendant = data['Attendant']
        quantity = data['Quantity']
        productId = data['product id']

        if Validators.empty_sales_fields(
                self, quantity, attendant, productId):
                return {'message':
                        "blank field not allowed"}

        for product in products:
            if productId == int(product['id']):
                price = product['Price'] * quantity

        for product in products:
            if productId == int(product['id']):
                payload = {
                    'id': id,
                    'Attendant': attendant,
                    'Quantity': quantity,
                    'product id': productId,
                    'Total price': price
                    }
        sales.append(payload)
        for product in products:
            if productId == int(product['id']):
                product['Stock Balance'] -= quantity

        return make_response(jsonify(
            {
                'Message': 'Sales created',
                'status': 'ok',
                'Data': sales
            }), 201)


class SignUp(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("email", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("password", type=str, required=True,
                        help="This field can not be left bank")

    @jwt_required
    @admin_only
    def post(self):
        """ Create a new user"""
        data = SignUp.parser.parse_args()

        email = data["email"]
        password = data["password"]

        validate = Validators()

        if not validate.valid_email(email):
            return {"message": "enter valid email"}, 400

        if not validate.valid_password(password):
            return {
                "message":
                "password should have a capital letter & includes number"
                }, 400

        if User().get_by_email(email):
            return {"message":
                    "user with {} already exists"
                    .format(email)}, 400

        user = User(email, password)
        Users.append(user)

        return {"message": "user {} created successfully".format(email)}, 201


class Login(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("email", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("password", type=str, required=True,
                        help="This field can not be left bank")

    def post(self):
        data = Login.parser.parse_args()

        email = data["email"]
        password = data["password"]

        user = User().get_by_email(email)

        if user and check_password_hash(user.password_hash, password):
            expires = datetime.timedelta(days=2)
            token = create_access_token(user.email, expires_delta=expires)
            return {'token': token, 'message': 'successfully logged'}, 200
        return {'message': 'user not found'}, 404
