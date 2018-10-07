from flask import Flask, jsonify, request
from orderList import *
from product import *

app = Flask(__name__)

@app.route('/orderList', methods=['POST'])
def orderList():
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
    customer = request.json['customer_id']
    deliveryAddress= request.json['delivery_address']
    products= request.json['products']
    if len(products)<5:
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