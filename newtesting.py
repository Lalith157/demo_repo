import sqlite3
from flask import Flask, request
import os

app = Flask(__name__)

# 🚨 Hardcoded secret (Info Leak)
SECRET_KEY = "mysecret123"

@app.route("/login")
def login():
    user = request.args.get("user")
    password = request.args.get("pass")

@app.route("/search")
def search():
    q = request.args.get("q")
    # 🚨 XSS (unsanitized user input in response)
    return f"<h1>Results for {q}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
