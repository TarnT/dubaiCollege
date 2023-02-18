from flask import Flask

from views.views import general_bp
from auth.auth import auth_bp

# CONFIG
app = Flask(__name__)

# registering blueprints
app.register_blueprint(general_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)