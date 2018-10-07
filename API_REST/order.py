from db import *

class Order:
    def __init__(self,customerId,deliveryAddress,products,orderId=None):
        if orderId==None:
            self.orderId=0
            self.customerId=customerId
            self.deliveryAddress=deliveryAddress
            self.products=products
            self.date=""
        else:
            self.orderId=orderId
            dbConn=DbConnection()
            sql="select customer_id, delivery_address, product_description, price, DATE_FORMAT(date(creation_date), '%d-%m-%Y') from order_ inner join order_detail where order_.order_id=%s and order_detail.order_id = order_.order_id;"
            val=(orderId, )
            dbConn.execute(sql, val)
            result=dbConn.fetchall()
            self.customerId=result[0][0]
            self.deliveryAddress=result[0][1]
            self.date=result[0][4]
            self.products=[]
            for p in result:
                self.products.append([p[2],p[3]])
    def createOrder(self):
        dbConn=DbConnection()
        sql = "INSERT INTO order_ (customer_id, delivery_address) VALUES (%s, %s)"
        val = (self.customerId,self.deliveryAddress)
        dbConn.execute(sql,val)
        dbConn.commit()
        self.orderId=dbConn.lastRowId()
        for i in self.products:
            sql = "INSERT INTO order_detail (product_description, price, order_id) VALUES (%s, %s, %s)"
            val = (i[0],i[1],self.orderId)
            dbConn.execute(sql,val)
        dbConn.commit()
        return 0
        
        
        
        
        