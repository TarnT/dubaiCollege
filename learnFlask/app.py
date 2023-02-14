import sqlite3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# flask (lowercase) is the library
# Flask (capitalised) is the foundation of the website
# remember to use names, not ID tags, for HTML forms


# initisialising application
app = Flask(__name__)
app.config["SECRET_KEY"] = "catsanddogs"
DATABASE = "SQL/users.db"

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password = request.form.get("inputPassword")
        print(email, password)

    return render_template("login.html")

@app.route("/sign-up", methods=["GET", "POST"])
def signUp():

    if request.method == "POST":
        email = request.form.get("inputEmail")
        password1 = request.form.get("inputPassword1")
        password2 = request.form.get("inputPassword2")

    return render_template("signUp.html")

if __name__ == "__main__":
    app.run(debug=True)