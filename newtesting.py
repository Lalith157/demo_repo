def connect_to_service():
    username = "admin"
    password = "supersecret"  # 🚨 Vulnerable: hardcoded passwordfgh
    print(f"Connecting as {username}...")
