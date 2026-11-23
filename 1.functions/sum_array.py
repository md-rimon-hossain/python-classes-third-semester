
# ফাংশন ব্যবহার করে লিস্টের ৫টি সংখ্যার যোগফল নির্ণয়
def add_numbers():
    list_of_numbers = []
    
    for i in range(5): 
        number = int(input("Enter a number:"))
        list_of_numbers.append(number)
        
    total_sum = sum(list_of_numbers)
    print("The sum of the numbers is:", total_sum)
    
add_numbers()
