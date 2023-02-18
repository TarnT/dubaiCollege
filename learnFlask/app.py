from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from views.views import general_bp
from auth.auth import auth_bp

# CONFIG
app = Flask(__name__)
app.config["EXPLAIN_TEMPLATE_LOADING"] = True
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db.init_app(app)

with app.app_context():
    db.create_all()

# registering blueprints
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)