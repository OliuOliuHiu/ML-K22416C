from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Cấu hình MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306  # Cổng MySQL (nếu không phải 3306, hãy thay đổi)
# app.config['MYSQL_UNIX_SOCKET'] = '/var/run/mysqld/mysqld.sock'  # Chỉ thêm nếu dùng socket

mysql = MySQL(app)

try:
    with app.app_context():
        conn = mysql.connection
        print("Connection is successful!")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        data = cursor.fetchall()
        print(data)
except Exception as e:
    print("Error = ", e)
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("MySQL is closed")