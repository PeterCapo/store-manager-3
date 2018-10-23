import re


class Validators:
    def valid_product_name(self, productName):
        '''confirming name input has numbers and letters only'''
        regex = "^[a-zA-Z0-9_]+$"
        return re.match(regex, productName)
