from flask import Flask
from werkzeug.security import generate_password_hash

from app.api.v1.validators import utils

Users = []


class User:

    user_id = 1

    def __init__(self, email=None, password=None,
                 admin=False):

        self.email = email
        if password:
            self.password_hash = generate_password_hash(password)
        self.admin = admin
        self.id = User.user_id

        User.user_id += 1

    def get_by_email(self, email):
        for user in Users:
            if user.email == email:
                return user
