class Item():
    def __init__(self, itemnum, itemname, itemprice, itemsize):
        self.itemnum=itemnum
        self.itemname=itemname
        self.itemprice=itemprice
        self.itemsize=itemsize

    def getItemNumber(self):
         return self.itemnum

    def getItemName(self):
         return self.itemname

    def getItemPrice(self):
        return self.itemprice

    def getItemSize(self):
        return self.itemsize

    def __str__(self):
        return self.itemname          