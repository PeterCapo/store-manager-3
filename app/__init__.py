import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity
from app.api.v1.models.users import authenticate, identity

from instance import config



def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = os.getenv("SECRET_KEY")
    
    jwt = JWT(app, authenticate, identity)
    
    from .api.v1 import version1 as v1

    app.register_blueprint(v1)

    return app