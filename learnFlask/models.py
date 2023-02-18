from app import db 
from datetime import datetime
from flask_login import UserMixin

class User(db.model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.integer, primary_key=True, autoincrement=True)
    email = db.Column(db.string, unique=True, nullable=False)
    password = db.Column(db.string, nullable=False)
    date_created = db.Column(db.Date(timezone=True), default=datetime.now())