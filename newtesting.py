username = "admin"
password = "12345"   # Hardcoded password

def login(user, pwd):
    if user == username and pwd == password:
        print("Login successful!")
    else:
        print("Login failed!")

# Example call
login("admin", "12345")
