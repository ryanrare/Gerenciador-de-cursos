# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from config import config

from .api import configure_api
from .db import init_db


def create_app(config_name):
    app = Flask('api-users-courses')

    app.config.from_object(config[config_name])

    ma = Marshmallow(app)

    ma.init_app(app)

    app.config['JWT_SECRET_KEY'] = config[config_name].SECRET_KEY
    jwt = JWTManager(app)

    configure_api(app)

    init_db(app)

    return app
