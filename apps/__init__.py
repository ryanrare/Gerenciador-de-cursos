# -*- coding: utf-8 -*-

from flask import Flask
from flask_marshmallow import Marshmallow
from config import config

from .api import configure_api
from .db import init_db


def create_app(config_name):
    app = Flask('api-users-courses')

    app.config.from_object(config[config_name])

    ma = Marshmallow(app)

    ma.init_app(app)
    init_db(app)

    configure_api(app)

    return app
