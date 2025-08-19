# broken_auth_demo.py
from flask import Flask, request, make_response, redirect, url_for, jsonify
import base64, time, hashlib, secrets

app = Flask(__name__)

# 🚨 Vulnerable: plaintext “database” (no hashing, no salting)
USERS = {
    "alice": "password123",
    "bob":   "qwerty",
}

# 🚨 Vulnerable: predictable reset tokens (md5 of email)
def insecure_reset_token(email):
    return hashlib.md5(email.encode()).hexdigest()

# 🚨 Vulnerable: unsigned, guessable session "token"
def insecure_session_token(username):
    # base64 of "username:epoch" (no signing, no expiration check)
    raw = f"{username}:{int(time.time())}"
    return base64.b64encode(raw.encode()).decode()

@app.route("/login")
cvb
