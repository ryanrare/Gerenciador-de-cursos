# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'uma string randômica e gigante')
    APP_PORT = os.getenv('APP_PORT', '5000')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't', 'yes', 'y']
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'postgresql://postgres:suasenha@localhost:5432/courses_system')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
