
# ১। ফাংশন ব্যবহার করে ত্রিভুজ ক্ষেত্রের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম লেখ।

import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)
    
a = int(input("Enter the a side of triangle: "))
b = int(input("Enter the second side of triangle: "))
c = int(input("Enter the third side of triangle: "))

triangle_area(10,21,14) 
