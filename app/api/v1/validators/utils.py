import time
from flask_restful import abort
import re


class Validators:
    def empty_fields(self, productName, price, stockBalance, category):
        if productName == "" or price == "":
            if stockBalance == "" or category == "":
                res = 'blank field not allowed'
            return res

    def empty_sales_fields(self, attendant, quantity, productId):
        if attendant == "" or quantity == "" or productId == "":
            res = 'blank field not allowed'
            return res

    def valid_password(self, password):
        """validate for password """
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, password)

    def valid_email(self, email):
        """ validate for email """
        return re.match("^[^@]+@[^@]+[^@]+$", email)
