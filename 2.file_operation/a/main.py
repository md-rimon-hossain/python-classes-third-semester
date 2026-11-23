def program():
    f = open("MyFile.txt", "w")

    f.write("line 1 from user")
    f.write("\n")
    f.write("line 2 from user ")
    f.write("\n")
    f.write("line 3 from user ")
    f.close()

    rf = open("MyFile.txt", "r")
    print(rf.read())

    rf.close()
    
program()


with open("upper.txt", "r") as f1:
    data = f1.read()
    
    count_capital = 0
    count_lower = 0
    count_digit = 0
    
    for ch in data:
        if ch.isupper():
            count_capital += 1
        elif ch.islower():
            count_lower += 1
        elif ch.isdigit():
            count_digit += 1
    
    print("upper", count_capital)                
    print("lower", count_lower)                
    print("digit", count_digit)   
    
    
                 
