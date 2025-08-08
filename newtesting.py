import os
def list_files():
    user_input = input("Enter directory: ")
    os.system("ls " + user_input)  # 🚨 Vulnerable: unsanitized user input

import sqlite3
def get_user_info(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"  # 🚨 Vulnerable: SQL Injection
    cursor.execute(query)
    return cursor.fetchall()

from flask import Flask, request

app = Flask(__name__)

@app.route('/xss')
def xss_vuln():
    name = request.args.get("name")
    return f"<html><body>Hello {name}</body></html>"  # 🚨 Vulnerable: reflected XSS

def connect_to_service():
    username = "admin"
    password = "supersecret"  # 🚨 Vulnerable: hardcoded password
    print(f"Connecting as {username}...")

import pick
def load_data():
    data = input("Paste your pickled data: ")
    obj = pickle.loads(data.encode())  # 🚨 Vulnerable: unsafe deserialization
    print("Loaded:", obj)


def read_file():
    filename = input("Enter filename to read: ")
    with open("uploads/" + filename, "r") as f:  # 🚨 Vulnerable: Path Traversal
        print(f.read())

if __name__ == "__main__":
    list_files()
    get_user_info("1 OR 1=1")
    connect_to_service()
    load_data()
    read_file()
