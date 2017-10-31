class Bike(object):
    def __init__(self,price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "The price is:", self.price
        print "The max speed is:", self.max_speed
        print "The mileage is:", self.miles
    def ride(self,rep):
        print "Riding x", rep
        self.miles += 10 * rep
    def reverse(self,rep):
        print "Reversing x",rep
        if(self.miles >=5*rep):
            self.miles -= 5 * rep

bike1 = Bike(200, "25 mph")
bike2 = Bike(300, "30 mph")
bike3 = Bike(400, "35 mph")

bike1.ride(3) 
bike1.reverse(1) 
bike1.displayInfo()

bike2.ride(2)
bike2.reverse(2)
bike2.displayInfo()

bike3.ride(0)
bike3.reverse(3)
bike3.displayInfo()