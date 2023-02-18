import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "kittens"
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    EXPLAIN_TEMPLATE_LOADING = True