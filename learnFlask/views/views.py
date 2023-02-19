from flask import Blueprint, render_template
import os

view_bp = Blueprint("view_bp", __name__, template_folder="templates/views")

@view_bp.route("/")
def index():
    return render_template("index.html")

