# vulnerable_xss.py
# Single intentional vulnerability: reflected XSS (no other insecure patterns)

from flask import Flask, request

app = Flask(__name__)

@app.route("/greet")
def greet():
    # VULNERABILITY: user input is inserted directly into HTML without escaping
    # This is a reflected XSS vulnerability.
    name = request.args.get("name", "Guest")
    return f"<html><body><h1>Hello, {name}!</h1></body></html>"

if __name__ == "__main__":
    app.run(debug=True)
