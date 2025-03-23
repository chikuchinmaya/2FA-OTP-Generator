# **2FA OTP Generator with MySQL Integration**

This project is a Two-Factor Authentication (2FA) OTP generator application. It provides a simple frontend and a Flask-based backend for adding secret keys and generating Time-based One-Time Passwords (TOTPs). The project is integrated with MySQL for persistent storage of secret keys.

---

## **Features**

- Add and store secret keys securely in a MySQL database.
- Generate and retrieve Time-based One-Time Passwords (TOTP).
- Frontend interface to interact with the backend.
- Auto-refresh OTPs every 30 seconds.
- Easy to deploy and scalable.

---

## **Technologies Used**

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript
- **Database**: MySQL
- **Dependencies**: 
  - `flask`
  - `pyotp`
  - `flask-cors`
  - `mysql-connector-python`

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.x installed on your system.
- MySQL Server installed and running.
- `pip` package manager for Python dependencies.

### **2. Clone the Repository**
```bash
git clone https://github.com/chikuchinmaya/2FA-OTP-Generator.git
cd 2fa-otp-generator

3. Set Up the MySQL Database
Log in to your MySQL server:

bash
mysql -u root -p
Create a new database:

sql
CREATE DATABASE otp_project;
Switch to the new database:

sql
USE otp_project;
Create a table for storing secret keys:

sql
CREATE TABLE secret_keys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    secret_key VARCHAR(255) NOT NULL
);
4. Install Dependencies
Run the following command to install the required Python packages:

bash
pip install -r requirements.txt
5. Configure the Backend
Make sure to update backend.py with your database credentials:

python
db_config = {
    'host': 'localhost',  # Change to your MySQL server address if hosted elsewhere
    'user': 'root',       # Your MySQL username
    'password': 'password',  # Your MySQL password
    'database': 'otp_project'  # Name of the database
}
6. Start the Backend
Run the Flask server:

bash
python3 backend.py
The backend will start at http://127.0.0.1:5000.

7. Open the Frontend
Open the index.html file in a browser to start using the application.

Project Structure
plaintext
otp-generator/
│
├── backend.py            # Backend application with Flask
├── index.html            # Frontend UI
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

