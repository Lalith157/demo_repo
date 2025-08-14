import sqlite3

def login(user, password):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # 🚨 Vulnerable: directly concatenating user input...
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{password}'"
    print("Executing query:", query)
    cursor.execute(query)

    result = cursor.fetchall()
    if result:
        print("Login successful!")
    else:
        print("Invalid credentials")

    conn.close()

# Example of SQL Injection payload
login("admin", "' OR '1'='1")
