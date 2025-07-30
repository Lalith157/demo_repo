import osfg
import sqlite3
import json
#dfgasdfdsdfdsdffdsaasdvdf

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # ❌ Vulnerability: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Invalid credentials")

def load_config():
    # ❌ Vulnerability: Hardcoded secret
    api_key = "sk_test_1234567890abcdef"
    print("API Key loaded:", api_key)

def run_shell():
    command = input("Enter a shell command: ")
    # ❌ Vulnerability: Command injection
    os.system(command)

def unsafe_json_parse():
    data = input("Enter JSON data: ")
    # ❌ Vulnerability: Unsafe eval
    parsed = eval(data)
    print("Parsed JSON:", parsed)

login()
load_config()
run_shell()
unsafe_json_parse()
