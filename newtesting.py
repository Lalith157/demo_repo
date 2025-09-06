from flask import Flask, request

app = Flask(__name__)

@app.route("/greet")
def greet()    # <-- SYNTAX ERROR: missing colon here
    name = request.args.get("name", "Guest")
    # VULNERABILITY: reflected XSS — user input placed directly into HTML without escaping
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
