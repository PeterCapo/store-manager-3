from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.db_con import connection

Users = []


class User():
    def __init__(self, email=None, password=None, admin=False):
        super().__init__()
        self.curr = connection().cursor()
        self.email = email
        if password:
            self.password_hash = generate_password_hash(password)
            self.admin = admin

    def save(self, email, password_hash, admin):

        users = {
            "email": self.email,
            "password": self.password_hash,
            "admin":self.admin
        }
        query = """INSERT INTO users(email, password, admin) VALUES( % s, % s, % s, % s)"""
        self.curr.execute(query, users)
        return users


    def get_by_email(self, email, password, admin):
        self.curr.execute(
            """SELECT * FROM users where email= %s""", (email,))
        data = self.curr.fetchone()
        resp = []
        user_id, email, password, admin = data
        user_return = dict(
            user_id=int(user_id),
            email=email,
            password=password,
            admin=admin
        )
        resp.append(user_return)

        return resp
