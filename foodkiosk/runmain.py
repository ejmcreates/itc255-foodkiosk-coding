from item import Item
from orderitem import OrderItem
from order import Order

def main():

    item1=Item(1,'chips',2.50,'med')
    item2=Item(2, 'pizza', 15.99, 'large')


    orderitem1=OrderItem(item1,1,'none')
    orderitem2=OrderItem(item2, 1, 'olives')

    order=Order()
    order.addOrderItems(orderitem1)
    order.addOrderItems(orderitem2)

    payment=order.calcTotal()
    print(payment)

    

main()    