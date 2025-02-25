from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "mariadb",
    "user": "root",
    "password": "rootpassword",
    "database": "testdb"
}

@app.route('/')
def index():
    return "Aplikasi Flask dengan MariaDB!"

@app.route('/users', methods=['GET'])
def get_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
