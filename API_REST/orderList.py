from order import *

class OrderList:
    def __init__(self,customerId=None,initDate=None,finalDate=None):
        if customerId==None:
            self.orderList=[]
        else:
            dbConn=DbConnection()
            sql="select DISTINCT order_.order_id from order_ inner join order_detail where customer_id = %s and date(creation_date)>=%s and date(creation_date)<=%s;"
            val=(customerId, initDate,finalDate)
            dbConn.execute(sql, val)
            self.orderList=[]
            result=dbConn.fetchall()
            for o in result:
                self.orderList.append(Order(None,None,None,int(o[0])))
                
