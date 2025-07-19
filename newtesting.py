from flask import Flask, request, send_from_directory, jsonify
d234rrfx
app = Flask(__name__)

# ❌ Hardcoded user credentials — bad practice
users = {
    'admin': 'admin123',
    'user': 'user123'
}

# ❌ Insecure login endpoint with no hashing or session
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # ❌ Broken Authentication: no password hashing, no rate limiting, no token
    if username in users and users[username] == password:
        return jsonify(message="Login successful!"), 200
    return jsonify(error="Invalid credentials"), 401

# ❌ Security Misconfiguration: open file access with no validation
@app.route('/files/<path:filename>')
def get_file(filename):
    return send_from_directory('.', filename)

# ❌ Security Misconfiguration: app runs in debug mode — RCE risk
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
