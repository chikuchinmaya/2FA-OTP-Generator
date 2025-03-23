from flask import Flask, jsonify, request
import pyotp
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection details
db_config = {
    'host': 'localhost',  # Change to your MySQL server address
    'user': 'root',       # Your MySQL username
    'password': 'password',  # Your MySQL password
    'database': 'otp_project'  # Name of your database
}

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return "Welcome to the OTP Generator with MySQL Integration!"

@app.route('/add-secret', methods=['POST'])
def add_secret():
    data = request.json
    secret_key = data.get('secretKey')
    if secret_key:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO secret_keys (secret_key) VALUES (%s)"
            cursor.execute(query, (secret_key,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Secret key added successfully!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Secret key is required!"}), 400

@app.route('/get-otps', methods=['GET'])
def get_otps():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT secret_key FROM secret_keys"
        cursor.execute(query)
        secret_keys = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()

        otps = [{"secretKey": key, "otp": pyotp.TOTP(key).now()} for key in secret_keys]
        return jsonify(otps), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
