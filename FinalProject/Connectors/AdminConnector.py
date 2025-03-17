from FinalProject.Connectors.Connector import Connector
from FinalProject.Models.Admin import Admin


class AdminConnector(Connector):
    def sign_in(self,username,password):
        cursor = self.conn.cursor()
        sql= "select * from admin where AdminAccount=%s and AdminPassword=%s"
        val = (username,password)
        cursor.execute(sql,val)
        dataset = cursor.fetchone()
        ad = None
        if dataset != None:
            AdminID , AdminFullName , AdminAccount , AdminPassword,AdminPhone = dataset
            ad = Admin(AdminID , AdminFullName , AdminAccount , AdminPassword,AdminPhone)
        cursor.close()
        return ad