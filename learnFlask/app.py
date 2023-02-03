import sqlite3
from flask import Flask, render_template

# flask (lowercase) is the library
# Flask (capitalised) is the foundation of the website

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/test")
def test():
    return "Should be a test."