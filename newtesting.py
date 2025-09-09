# vulnerable_xss.py

username = "admin"   # Hardcoded username
password = "12345"   # Hardcoded password

from flask import Flask, request

app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"<html><body><h1>Hello, {name}!</h1></body></html>"   # Reflected XSS
