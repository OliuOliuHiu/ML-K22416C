import mysql.connector
import traceback
import pandas as pd
class Connector:
    def __init__(self,server=None, port=None, database=None, username=None, password=None):
        self.server=server
        self.port=port
        self.database=database
        self.username=username
        self.password=password
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password)
            return self.conn
        except:
            self.conn=None
            traceback.print_exc()
        return None

    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    '''def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns=cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None'''

    def queryDataset(self, sql, fetch_data=True):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)

            # Nếu fetch_data là True, nghĩa là muốn lấy dữ liệu trả về từ truy vấn
            if fetch_data:
                df = pd.DataFrame(cursor.fetchall())
                if not df.empty:
                    df.columns = cursor.column_names
                return df
            else:
                # Trường hợp không muốn lấy dữ liệu, chỉ cần commit thay đổi vào cơ sở dữ liệu
                self.conn.commit()
                return True
        except:
            traceback.print_exc()
            return None
