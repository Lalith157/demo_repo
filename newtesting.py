# vuln_demo.py  (intentionally insecure – for testing only)

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

    # 🚨 SQL Injection (unsafe string concatenation)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + user + "' AND password = '" + password + "';"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        return "Login successful"
    else:
        return "Login failed"

@app.route("/cmd")
def run_command():
    # 🚨 Command Injection (os.system with user input)
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "Executed: " + cmd

@app.route("/search")
def search():
    q = request.args.get("q")
    # 🚨 XSS (unsanitized user input in response)
    return f"<h1>Results for {q}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
