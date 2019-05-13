from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.db_con import connection


products =[]

class Product():
    def __init__(self, product_id = None):
        self.curr = connection().cursor()
        self.product_id = product_id
    
    def save(self, product_id, productName, stockBalance, price, category):

        payload = {
            "Product Name": productName,
            "Price": price,
            "Stock Balance": stockBalance,
            "Category": category
        }
        query = """INSERT INTO products (productname, price, stockBalance, category) VALUES
                (%(Product Name)s, %(Price)s, %(Stock Balance)s, %(Category)s)"""
        self.curr.execute(query, payload)
        return payload

    def getproducts(self):
        self.curr.execute(
            """SELECT product_id, productName, price, stockBalance, category FROM products""")
        data = self.curr.fetchall()
        resp = []

        for  products in data:
            product_id, productName, price, stockBalance, category = products
            datar = dict(
                product_id=int(product_id),
                productName=productName,
                stockBalance=int(stockBalance),
                Price=int(price),
                Category=category
            )
            resp.append(datar)

        return resp
    
    def get_one_product(self, product_id):
        self.curr.execute(
            """SELECT * FROM products where product_id = %s""",(product_id,))
        data = self.curr.fetchone()
        resp = []

        product_id, productName, category, price, stockBalance = data
        product_return = dict(
            product_id=int(product_id),
            productName=productName,
            stockBalance=int(stockBalance),
            Price=int(price),
            Category=category
           )
        resp.append(product_return)

        return resp
    
    def update_product(self, productName, category, price, stockBalance, product_id):
        payload = {
            "Product Name": productName,
            "Category": category,
            "Price": price,
            "Stock Balance": stockBalance
        }
        query = """UPDATE products set productName =%s, category =%s, price=%s, stockBalance= %s where product_id = %s """
        self.curr.execute(query,  (productName, category, price, stockBalance, product_id))
        return payload
    
    def delete(self, product_id):
        """ delete product item """
        self.curr.execute(
            """DELETE FROM products WHERE product_id = %s""", (product_id,)
        )

        return product_id
