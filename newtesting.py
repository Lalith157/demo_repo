# vuln_demo.py  (intentionally insecure – for testing only)
from flask import Flask, request, jsonify
import sqlite3, os, hashlib, base64, time, pickle

app = Flask(__name__)

# CWE-798: Hardcoded credentials / weak defaults
USERS = {"admin": "admin123", "alice": "password"}  # ❌ do NOT do this

# CWE-327: Weak hashing for “tokens”
def insecure_reset_token(email):
    return hashlib.md5(email.encode()).hexdigest()  # ❌ MD5 is broken

# tiny demo db
def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE IF NOT EXISTS users (u TEXT, p TEXT)")
    conn.execute("DELETE FROM users")
    for u, p in USERS.items():
        conn.execute("INSERT INTO users (u,p) VALUES (?,?)", (u, p))
    conn.commit()
    return conn

@app.route("/login")
def login():
    # CWE-89: SQL injection (string concatenation)
    u = request.args.get("u", "")
    p = request.args.get("p", "")
    conn = get_db()
    # ❌ vulnerable: direct string interpolation
    query = f"SELECT * FROM users WHERE u='{u}' AND p='{p}'"
    try:
        row = conn.execute(query).fetchone()
        return jsonify(ok=bool(row), query=query)
    finally:
        conn.close()

if __name__ == "__main__":
    # dev only
    app.run(debug=True, port=5000)
