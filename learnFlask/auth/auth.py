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

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash:
                check_password_hash(user.password, password):
                flash("Logged in!", category="error")
                login_user(user, remember=True)
                return redirect(url_for("views.index"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect email.")

    return render_template("login.html")

@auth_bp.route("/sign-up", methods=["GET", "POST"])
def signUp():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password1 = request.form.get("inputPassword1")
        password2 = request.form.get("inputPassword2")
        
        exists = User.query.filter_by(email=email).first() is not None
        if exists:
            flash("Email already exists!", category="error")
        elif password1 != password2:
            flash("Passwords don't match!", category="error")
        else:

            # Add the user to the Database
            new_user = User(email=email, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("User Created!")
            login_user(new_user, remember=True)
            return redirect(url_for("views.index"))

        # TODO implement checks for passwords and email
        
        # TODO implement notice for user for incorrect info


    return render_template("signUp.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.index"))