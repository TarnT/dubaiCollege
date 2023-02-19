# TODO implement username 

from flask import Blueprint, render_template
from flask_login import login_required, current_user

view_bp = Blueprint("view_bp", __name__, template_folder="templates/views")

@view_bp.route("/")
@login_required
def index():
    return render_template("index.html")

