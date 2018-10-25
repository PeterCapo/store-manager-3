from flask_restful import Api
from flask import Blueprint


from .views import Sales, Products
from .views import SpecificProduct, SpecificSale
from .views import UpdateProduct, Login
from .views import SignUp

version1 = Blueprint('api', __name__, url_prefix='/api/v1')


api = Api(version1)


api.add_resource(Sales, '/sales')
api.add_resource(Products, '/products')
api.add_resource(SpecificProduct, '/products/<int:id>')
api.add_resource(SpecificSale, '/sales/<int:id>')
api.add_resource(UpdateProduct, '/products/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(SignUp, '/signup')
