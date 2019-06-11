import unittest
from item import Item
from orderitem import OrderItem
from order import Order

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(1,'chips',3.75, 'med')

    def test_itemString(self):
        self.assertEqual(str(self.item),self.item.itemname)

    def test_getPrice(self):
        self.assertEqual(str(self.item.getItemPrice()), '3.75')

    def test_getItemNumber(self):
        self.assertEqual(str(self.item.getItemNumber()),'1')

class OrderItemTest(unittest.TestCase):
    def setUp(self): 
        self.item=Item(1,'chips',3.75, 'med')
        self.quantity=2
        self.special='none'
        self.orderitem=OrderItem(self.item, self.quantity, self.special) 

    def test_getQuantity(self):
        self.assertEqual(self.orderitem.getQuantity(),2)    

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.o=Order()
        self.item1=Item(1,'chips', 4.00, 'med')
        self.item2=Item(2,'pizza', 13.00, 'small')
        self.item3=Item(3,'fries', 2.00, 'small')

        self.orderitem1=OrderItem(self.item1,2,'none')
        self.orderitem2=OrderItem(self.item2,1,'none')
        self.orderitem3=OrderItem(self.item3,3,'none')

        self.o.addOrderItems(self.orderitem1)
        self.o.addOrderItems(self.orderitem2)
        self.o.addOrderItems(self.orderitem3)

    def test_CalculateTotal(self):
        payment=self.o.calcTotal()
        self.assertEqual(str(payment), 'Your payment today will be 27.0')    

