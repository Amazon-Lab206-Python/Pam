class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12

        self.displayAll()

    def displayAll(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

car1 = Car(5000, "60 mph", "Full", 30000)
car2 = Car(7000, "50 mph", "Half", 50000)
car3 = Car(12000, "100 mph", "Empty", 100000)
car4 = Car(25000, "160 mph", "Full", 2000)
car5 = Car(150000, "30 mph", "Empty", 5)
car6 = Car(3000, "35 mph", "Half", 75000)
