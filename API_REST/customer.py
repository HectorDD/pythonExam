from db import *

class Customer:
    def __init__(self,customerId,name="",email=""):
        self.customerId=customerId
        self.name=name
        self.email=email
        dbConn=DbConnection()
        sql="select product_id from products_customer where customer_id=%s;"
        val=(customerId, )
        dbConn.execute(sql, val)
        self.products=[]
        for i in dbConn.fetchall():
            self.products.append(i[0])

      
