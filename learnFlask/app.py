from flask import Flask

from views.views import general_bp

# CONFIG
app = Flask(__name__)

# registering blueprints
app.register_blueprint(general_bp, url_prefix="/")


'''
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
'''

if __name__ == "__main__":
    app.run(debug=True)