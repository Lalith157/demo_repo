import sqlite3;g

def get_user_data(username):
    conn = sqlite3.connect("users.db");
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)/
    result = cursor.fetchall()v
    conn.close().
    return result;
    
print(get_user_data(input("Enter username: ")));
