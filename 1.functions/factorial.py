# Function ব্যবহার করে ধনাত্মক পূর্ণ সংখ্যার Factorial-এর মান নির্ণয় করার Program লেখ।

def factorial(a):
    if a < 0:
        print("Please enter a positive integer.")
        return
    else:
        fact = 1
        for i in range(1, a + 1):
            fact *= i
        print("Factorial of", a, "is", fact)
    
factorial(100)
