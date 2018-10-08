from flask import Flask, jsonify, request
from orderList import *
from product import *
from customer import *

app = Flask(__name__)

@app.route('/orderList', methods=['POST'])
def orderList():
    """Devuelve una lista con las ordenes realizadas por un usuario en un rango de fechas.
    
    Entradas:
    init_date: Fecha inicial en el rango de fechas (yyyy-mm-dd).
    
    final_date: Fecha final en el rango de fechas (yyyy-mm-dd).
    
    customer_id: ID del cliente para el cual se desea consultar las ordenes.
    
    Salidas:
    result: Lista de ordenes.
    
    EJEMPLO:
    
    Entradas:
    {
        "init_date" : "2017-01-01",
        "final_date" : "2019-01-01",
        "customer_id" : "2"
    }
    
    Salidas:
    {
        "result" : [{"date" : "2018-10-07", "order_id" : "3", "price" : "4350", 
        "delivery_address" : "8897", "products" : ["productA X2", "productB X3"]},
        {"date" : ...}]
    } 
    
    """
    initDate=request.json['init_date']
    finalDate=request.json['final_date']
    customerId=request.json['customer_id']
    oList=OrderList(customerId,initDate,finalDate)
    result=[]
    for o in oList.orderList:
        products=[]
        price=0
        for p in o.products:
            products.append(p[0])
            price+=p[1]
        result.append({'date' : o.date, 'order_id' : o.orderId, 'price' : price, 'delivery_address' : o.deliveryAddress,'products' : products})
    return jsonify({'result' : result}) 
    
@app.route('/createOrder', methods=['POST'])
def createOrder():
    """Crea una orden en la base de datos.
    
    Entradas:
    customer_id: ID del cliente que realiza la orden.
    
    delivery_address: Dirección de la orden.
    
    products: Lista de productos para la orden. Cada producto es
    una lista con el ID del producto y la cantidad del mismo.
    
    Salidas:
    result: 0 si todo sale bien, 1 si hay algún problema.
    
    EJEMPLO:
    
    Entradas:
    {
	    "customer_id":"2",
	    "delivery_address":"192",
	    "products":[["2",10],["3",15]]
    }
    
    Salidas:
    {
        "result":"0"
    }
    
    """
    customer = request.json['customer_id']
    deliveryAddress= request.json['delivery_address']
    products= request.json['products']
    customerObj=Customer(customer)
    validOrder=True
    for i in products:
        if not int(i[0]) in customerObj.products:
            validOrder=False
    if len(products)<5 and validOrder:
        orderProducts=[]
        for p in products:
            product=Product(p[0])
            productDescription=product.name + " X" + str(p[1])
            price = product.unitPrice * p[1]
            orderProducts.append([productDescription,price])
        currentOrder=Order(customer,deliveryAddress,orderProducts)
        currentOrder.createOrder()
        return jsonify({'result' : '0'})
    else:
        return jsonify({'result' : '1'})
    
if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8082)