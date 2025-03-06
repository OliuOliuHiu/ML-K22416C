import mysql.connector

class MySQLConnector:
    def __init__(self, server="localhost", port=3306, database="salesdatabase",
                 username="root", password="123456"):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password
            )
            return self.conn
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)
            return None

    def close(self):
        if self.conn:
            self.conn.close()
