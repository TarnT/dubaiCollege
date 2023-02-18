from flask import Blueprint, render_template
import os

general_bp = Blueprint("general_bp", __name__, template_folder="templates/views")

@general_bp.route("/")
def index():
    return render_template("index.html")

