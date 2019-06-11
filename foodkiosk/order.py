from item import Item
from orderitem import OrderItem

class Order():
    def __init__(self):
        self.orderitems=[]

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def getOrderItems(self):
        return self.orderitems

    def calcTotal(self):
        total=0.0
        for o in self.orderitems:
            total +=o.getItem().itemprice * o.quantity

        response="Your payment today will be " + str(round(total,2))
        return response            