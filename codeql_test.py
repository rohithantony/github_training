from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    conn = sqlite3.connect("users.db")

    # Vulnerable: user-controlled input is directly concatenated into SQL
    query = "SELECT id, username, email FROM users WHERE username = '" + username + "'"

    cursor = conn.execute(query)
    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({
            "id": user[0],
            "username": user[1],
            "email": user[2]
        })

    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()