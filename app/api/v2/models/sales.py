from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.db_con import connection

sales=[]
class Sale():
    def __init__(self):
        self.curr = connection().cursor()

    def save(self, attendant,
             quantity,
             productId,
             ):

        payload = {
            "Attendant": attendant,
            "Quantity": quantity,
            "product id": productId,
        }
        query = """INSERT INTO sales (attendant, quantity, productId) VALUES
                (%(Attendant)s, %(Quantity)s, %(product id)s)"""
        self.curr.execute(query, payload)
        return payload

    def getsales(self):
        self.curr.execute(
            """SELECT sales_id, attendant, quantity, productId FROM sales;""")
        data = self.curr.fetchall()
        resp = []

        for sale in data:
            sale_id, attendant, quantity, productId = sale
            sale_return = dict(
                sale_id=int(sale_id),
                attendant=attendant,
                quantity=int(quantity),
                productId=int(productId)
            )
            resp.append(sale_return)

        return resp
