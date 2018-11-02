import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager

from instance.config import app_config

jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.secret_key = os.getenv("SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    

    jwt.init_app(app)

    from .api.v2 import version2 as v2
    app.register_blueprint(v2)

    return app
