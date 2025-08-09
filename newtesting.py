import sqlite3

def get_user_info(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🚨 Vulnerable: Directly concatenating user input into SQL query
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)

    results = cursor.fetchall()
    conn.close()
    return results

# Example usage
print(get_user_info("1 OR 1=1"))  # This would dump all users
