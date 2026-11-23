
with open("info.txt","r") as file:
    with open("upper.txt","w") as new:
        for line in file:
            new.write(line.upper())
    
print("converted to uppercase...😊")

file = open("upper.txt","r")
print(file.read())
file.close()
