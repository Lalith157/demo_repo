import json
import random

def generate_samples():
    samples = []

    # ---------- Weak Default Credentials (5 samples) ----------
    default_creds = [
        ("admin", "admin"),
        ("root", "root"),
        ("user", "password"),
        ("test", "test123"),
        ("guest", "guest"),
    ]
    for i, (u, p) in enumerate(default_creds, 1):
        samples.append({
            "id": f"weak_default_creds_{i}",
            "language": "Python",
            "vulnerability": "Weak Default Credentials",
            "description": "Hardcoded weak default credentials allow unauthorized access.",
            "code": f'''# 🚨 Vulnerable: Weak default credentials
def login(username, password):
    DEFAULT_USER = "{u}"
    DEFAULT_PASS = "{p}"
    if username == DEFAULT_USER and password == DEFAULT_PASS:
        print("Login successful with default credentials!")
    else:
        print("Access denied")'''
        })

    # ---------- Weak Password Policies (5 samples) ----------
    weak_pw_policies = [
        "len(password) >= 3",   # too short
        "password.isdigit()",   # only numbers
        "password.isalpha()",   # only letters
        "'123' in password",    # trivial substring check
        "password == 'password'" # literally 'password'
    ]
    for i, rule in enumerate(weak_pw_policies, 1):
        samples.append({
            "id": f"weak_pw_policy_{i}",
            "language": "Python",
            "vulnerability": "Weak Password Policy",
            "description": "Insecure password policy allows trivial or guessable passwords.",
            "code": f'''# 🚨 Vulnerable: Weak password policy
def validate_password(password):
    if {rule}:
        return True
    return False
print(validate_password("1234"))  # Insecurely passes'''
        })

    # ---------- Weak Secret (1 sample) ----------
    samples.append({
        "id": "weak_secret_1",
        "language": "Python",
        "vulnerability": "Weak Secret",
        "description": "Hardcoded weak secret key used for session signing.",
        "code": '''# 🚨 Vulnerable: Hardcoded weak secret
SECRET_KEY = "12345"

def get_secret():
    return SECRET_KEY
print("Using secret key:", get_secret())'''
    })

    # ---------- WSGI Input Manipulation (1 sample) ----------
    samples.append({
        "id": "wsgi_input_manipulation_1",
        "language": "Python",
        "vulnerability": "WSGI Input Manipulation",
        "description": "Directly trusting wsgi.input without validation enables request smuggling.",
        "code": '''# 🚨 Vulnerable: Directly trusting wsgi.input
def application(environ, start_response):
    input_data = environ['wsgi.input'].read(1024)  # attacker controls this
    # blindly echo input
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Received: " + input_data]
'''
    })

    return samples

if __name__ == "__main__":
    vuln_samples = generate_samples()
    with open("synthetic_python_vulns.jsonl", "w", encoding="utf-8") as f:
        for s in vuln_samples:
            f.write(json.dumps(s) + "\n")
    print(f"[INFO] Generated {len(vuln_samples)} samples into synthetic_python_vulns.jsonl")
