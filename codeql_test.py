import sqlite3

def search_user():
    username = input("Enter username: ")

    conn = sqlite3.connect("users.db")

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor = conn.execute(query)
    print(cursor.fetchall())

if __name__ == "__main__":
    search_user()