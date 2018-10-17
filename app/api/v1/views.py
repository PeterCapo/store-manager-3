from flask_restful import Resource
from flask import Flask, jsonify, make_response, request

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
