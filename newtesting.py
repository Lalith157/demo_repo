from flask import Flask, request, session, abort

app = Flask(__name__)
app.secret_key = "secure_random_key_12345"  # Replace with a secure key,,,

# Simulated user database...
users = {
    "alice": {"role": "user", "data": "Alice's private data", "password": "alice123"},
    "bob": {"role": "user", "data": "Bob's private data", "password": "bob123"},
    "admin": {"role": "admin", "data": "Admin's sensitive data", "password": "admin123"}
}

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and users[username]["password"] == password:
        session["username"] = username
        session["role"] = users[username]["role"]
        return "Logged in successfully"
    return "Invalid credentials", 401

@app.route("/get_data", methods=["GET"])
def get_data():
    if "username" not in session:
        abort(401, "Unauthorized: Please log in")
    
    requested_username = request.args.get("username")
    current_user = session["username"]
    
    # Restrict access: users can only access their own data, admins can access all
    if session["role"] == "admin" or current_user == requested_username:
        if requested_username in users:
            return users[requested_username]["data"]
        return "User not found", 404
    abort(403, "Forbidden: You can only access your own data")

if __name__ == "__main__":
    app.run(debug=True)
