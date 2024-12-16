from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})


# MySQL connection
db_config = {
    "host": "db",
    "user": "root",
    "password": "rootpassword",
    "database": "testdb",
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        new_data = request.json.get('data', '')
        cursor.execute("INSERT INTO items (name) VALUES (%s)", (new_data,))
        conn.commit()
        return jsonify({"message": "Data inserted"}), 201
    
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3030)
