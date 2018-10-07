import mysql.connector

class DbConnection:
    def __init__(self):
        self._connection=mysql.connector.connect(
        host="localhost",
        user="hectordavid1228",
        passwd="",
        database="python_exam"
        )
        self._cursor=self.connection.cursor()
    def __del__(self):
        self.connection.close()
    
    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor  
    def execute(self,command,values=None):
        self._cursor.execute(command, values)
    def commit(self):
        self._connection.commit()
    def lastRowId(self):
        return self._cursor.lastrowid
    def fetchall(self):
        return self.cursor.fetchall()
"""      
dbConn=DbConnection()
sql = "INSERT INTO order_ (customer_id, delivery_address) VALUES (%s, %s)"
val = ("1","77")
dbConn.execute(sql,val)
dbConn.commit()
"""
        


