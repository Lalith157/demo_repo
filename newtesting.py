def connect_to_service():
    username = "admin"
    password = "supersecret"  # 🚨 Vulnerable: hardcoded password
    print(f"Connecting as {username}...")
