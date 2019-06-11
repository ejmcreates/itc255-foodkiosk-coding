from item import Item

class OrderItem():
    def __init__(self, item, quantity, special):
        self.item=item
        self.quantity=quantity
        self.special=special    

    def getItem(self):
        return self.item

    def getQuantity(self):
        return self.quantity

    def getSpecial(self):
        return self.special    