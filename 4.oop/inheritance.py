class Vehicle: 
    def __init__(self, name):
            self.name = name
            
    def run(self):
        print(self.name,"is running")
    
class Car(Vehicle):
    def start(self):
        print(self.name,"started")
 
class Bike(Car):
    def start(self):
        print(self.name,"started")
        
        
        
car1 = Car("BMW 1")
bike1 = Bike("R15 1")
print(car1.start())
print(car1.run())

print(bike1.start())
print(bike1.run())

