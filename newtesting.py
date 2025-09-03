# xss_demo.py  (intentionally insecure – for testing only)

from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    # 🚨 XSS vulnerability: user input is directly embedded in HTML
    return f"<h1>Search results for: {query}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
