import sqlite3

def get_user_info(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"  # 🚨 Vulnerable: SQL Injection///
    cursor.execute(query)
    return cursor.fetchall()
