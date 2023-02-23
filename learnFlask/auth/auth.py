from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from learnFlask.models import db
from learnFlask.models import User

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")

@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password = request.form.get("inputPassword")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("view_bp.index"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect email.")

    return render_template("login.html")

@auth_bp.route("/sign-up", methods=["GET", "POST"])
def signUp():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        username = request.form.get("username")
        password1 = request.form.get("inputPassword1")
        password2 = request.form.get("inputPassword2")
        
        emailExists = User.query.filter_by(email=email).first() is not None
        usernameExists = User.query.filter_by(username=username).first() is not None

        if emailExists:
            flash("Email already exists!", category="error")
        elif usernameExists:
            flash("Username already exists", category="error")
        elif password1 != password2:
            flash("Passwords don't match!", category="error")
        else:

            # Add the user to the Database
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("User Created!", category="success")
            login_user(new_user, remember=True)
            print("user created")
            return redirect(url_for("view_bp.index"))

        # TODO implement checks for passwords and email
        
        # TODO implement notice for user for incorrect info


    return render_template("signUp.html")

@auth_bp.route("/logout")
@login_required
def logout():
    # logout user and return them to the home page
    logout_user()
    return redirect(url_for("view_bp.index"))