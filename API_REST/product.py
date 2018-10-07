from db import *

class Product:
    def __init__(self,productId):
        self.productId=productId
        dbConn=DbConnection()
        sql="select name, unit_price from product where product_id=%s;"
        val=(productId, )
        dbConn.execute(sql, val)
        result=dbConn.fetchall()
        self.name=result[0][0]
        self.unitPrice=result[0][1]
"""
product=Product("2")
print(product.unitPrice)
print(product.name)
"""