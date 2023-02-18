from flask import Blueprint, render_template, request, flash 
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from models import User

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")

@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password = request.form.get("inputPassword")


    return render_template("login.html")

@auth_bp.route("/sign-up", methods=["GET", "POST"])
def signUp():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password1 = request.form.get("inputPassword1")
        password2 = request.form.get("inputPassword2")
        
        exists = User.query.filter_by(email=email).first() or False 
        if exists:
            flash("Email already exists!", category="error")
        elif password1 != password2:
            flash("Passwords don't match!", category="error")
        else:

            # Add the user to the Database
            new_user = User(email=email, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()

        flash("User Created!")
        return redirect(url_for("views.index"))

        # TODO implement checks for passwords and email


    return render_template("signUp.html")