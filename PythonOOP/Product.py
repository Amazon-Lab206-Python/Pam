class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self,num):
        self.price = self.price + (self.price * num)
        return self

    def return_reason(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "like new":
            self.status = "for sale"
        elif reason == "open":
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
        return self

    def displayInfo(self):
        print "Price:", self.price
        print "Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
