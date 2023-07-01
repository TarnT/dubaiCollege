from flask import Flask
from flask_login import LoginManager

from .config import Config

def create_app(test_config=None):

    # CONFIG
    app = Flask(__name__)
    app.config.from_object(Config)
    from .models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from learnFlask.models import User

    login_manager = LoginManager()
    login_manager.login_view = "auth_bp.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    # importing blueprints
    from .views.views import view_bp
    from .auth.auth import auth_bp

    # registering blueprints
    app.register_blueprint(view_bp)
    app.register_blueprint(auth_bp)

    return app