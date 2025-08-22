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

@app.route("/run")
def run():
    # CWE-78: Command injection
    cmd = request.args.get("cmd", "echo hello")
    # ❌ vulnerable: passes untrusted string to shell
    code = os.system(cmd)
    return jsonify(ran=cmd, exit_code=code)

@app.route("/read")
def read():
    # CWE-22: Path traversal
    path = request.args.get("path", "vuln_demo.py")
    # ❌ vulnerable: no validation of path
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read(200)
        return jsonify(path=path, preview=data)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route("/calc")
def calc():
    # CWE-94: Code injection via eval
    expr = request.args.get("expr", "1+1")
    # ❌ vulnerable: evaluating untrusted input
    try:
        result = eval(expr)
        return jsonify(expr=expr, result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route("/token")
def token():
    # CWE-345/345-ish: Guessable/unsigned session tokens
    user = request.args.get("user", "guest")
    raw = f"{user}:{int(time.time())}"
    tok = base64.b64encode(raw.encode()).decode()  # ❌ predictable/unsigned
    return jsonify(token=tok)

@app.route("/load")
def load():
    # CWE-502: Insecure deserialization
    blob_b64 = request.args.get("blob", "")
    try:
        # ❌ vulnerable: unpickling attacker-controlled data
        obj = pickle.loads(base64.b64decode(blob_b64))
        return jsonify(loaded=str(obj))
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    # dev only
    app.run(debug=True, port=5000)
