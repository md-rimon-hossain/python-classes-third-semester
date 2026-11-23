import math
class MyClass:
    def __init__(self, a, b, c ):
        
        d = (b * b) - (4 * a * c)
        
        if d < 0:
            print("Roots are not possible")
        else: 
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            
            print("x1 = ", x1)
            print("x2 = ", x2)
            
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

MyClass(a,b,c)

