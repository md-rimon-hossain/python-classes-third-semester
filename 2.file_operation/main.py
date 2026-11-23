file = open("info.txt","r")
new = open("upper.txt","w")

for line in file:
    new.write(line.upper())
    
file.close()
new.close()
print("converted to uppercase...")

file = open("upper.txt","r")
print(file.read())
file.close()


