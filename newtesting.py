from pymongo import MongoClient

def find_user(username, password):
    client = MongoClient("mongodb://localhost:27017/")
    db = client.test_db

    # 🚨 Vulnerable: Directly passing user input to queryy
    query = {"username": username, "password": password}
    user = db.users.find_one(query)
    
    if user:
        print("Login successful!")
    else:
        print("Invalid credentials.")
find_user({"$ne": None}, {"$ne": None})
