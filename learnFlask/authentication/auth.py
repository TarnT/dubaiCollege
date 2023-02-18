from flask import Blueprint, render_template

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login")
def login():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password = request.form.get("inputPassword")
        print(email, password)

    return render_template("login.html")