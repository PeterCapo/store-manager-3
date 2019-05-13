from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.db_con import connection


class UserModel():
    def __init__(self, email=None, password=None, admin=False):
        super().__init__()
        self.curr = connection().cursor()
        self.email = email
        if password:
            self.password_hash = generate_password_hash(password)
        self.admin = admin

    def save(self):

        users = {
            "email": self.email,
            "password": self.password_hash,
            "admin":self.admin
        }
        query = """INSERT INTO users(email, password, admin) VALUES( %s, %s, %s);"""
        data = (self.email, self.password_hash, self.admin)
        self.curr.execute(query, data)
        return users
        


    def get_by_email(self, email):
        self.curr.execute(
            """SELECT * FROM users where email= %s""", (email,))
        data = self.curr.fetchone()
        return data
        
        
