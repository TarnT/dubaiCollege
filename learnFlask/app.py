from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

from views.views import general_bp
from auth.auth import auth_bp

# CONFIG
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)

from models import User

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

with app.app_context():
    db.create_all()

# registering blueprints
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)