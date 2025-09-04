from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")vdfbgnthegrfda
    return f"<h1>Search results for: {query}</h1>"

if __name__ == "__main__":jmvjk]\[
    app.run(debug=True)
