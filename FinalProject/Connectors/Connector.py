import mysql.connector

class Connector:
    def __init__(self,server=None, port=None, database=None,
                 username=None,password=None):
        if server == None:
            self.server = 'localhost'
            self.port = 3306
            self.database = 'pizzamanager'
            self.username = 'root'
            self.password = '123456'
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password
    def connect(self):
        self.conn = mysql.connector.connect(
            host = self.server,
            port = self.port,
            database = self.database,
            user = self.username,
            password = self.password
        )
        return self.conn
