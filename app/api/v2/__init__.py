from flask_restful import Api
from flask import Blueprint


from .views import Products, Sales, Login
from .views import SpecificProduct, SpecificSale
from .views import UpdateProduct, SignUp


version2 = Blueprint('api2', __name__, url_prefix='/api/v2')


api = Api(version2)


api.add_resource(Products, '/product')
api.add_resource(Sales, '/sales')
api.add_resource(SpecificProduct, '/products/<int:id>')
api.add_resource(SpecificSale, '/sales/<int:id>')
api.add_resource(UpdateProduct, '/products/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(SignUp, '/signup')
