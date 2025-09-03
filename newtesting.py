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

@app.route("/cmd")
def run_command():
    # 🚨 Command Injection (os.system with user input)
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "Executed: " + cmd
