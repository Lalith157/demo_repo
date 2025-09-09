username = "admin"
password = "12345"

def login(user, pwd):
    if user == username and pwd == password:
        print("Login successful!")
    else:
        print("Login failed!")
