from app import db 
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.model):
    id = db.Column(db.integer, primary_key=True, autoincrement=True)
    email = db.Column(db.string, nullable=False)
    password = db.Column(db.string, nullable=False)