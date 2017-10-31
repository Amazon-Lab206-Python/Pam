class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self,rep):
        self.health -= 1 * rep
        return self
    def run(self,rep):
        self.health -= 5*rep
        return self
    def displayHealth(self):
        print "Health:", self.health
        return self 

# animal1 = Animal("cat", 20)

# animal1.walk(3).run(2).displayHealth()

class Dog(Animal):
    def __init__(self):
        self.health = 150
    def pet(self):
        self.health +=5
        return self

# dog1 = Dog()
# dog1.walk(3).run(2).pet().displayHealth()

class Dragon(Animal):
    def __init__(self):
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

# dragon1 = Dragon()
# dragon1.fly().displayHealths()

class Cat(Animal):
    def __init__(self):
        self.health = 10

cat1 = Cat()
cat1.displayHealth()
