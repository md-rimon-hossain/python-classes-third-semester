import math

class MyClass:
    def __init__(self, a, b, c ):
        self.a = a 
        self.b = b
        self.c = c
        
    def d(self): 
        
        d = (self.b * self.b) - (4 * self.a * self.c)
        
        if d < 0:
            print("Roots are not possible")
        else: 
            x1 = (-self.b + math.sqrt(d))/ (2*self.a)
            x2 = (-self.b - math.sqrt(d))/ (2*self.a)
            print("Roots are possible")
            print("x1 = ", x1)
            print("x2 = ", x2)
            


a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

obj = MyClass(a, b, c)
obj.d()