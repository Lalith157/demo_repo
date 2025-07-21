import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/run', methods=['GET'])
def run_command():=.
    cmd = request.args.get('cmd')  # ❌ No input validations
    os.system(cmd)  # ❌ Command Injection vulnerability
    return f"Executed: {cmd}"

app.run(host='0.0.0.0', port=5000)  # ❌ Exposes app to external access
