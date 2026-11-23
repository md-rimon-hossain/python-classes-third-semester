
file = open("student_info.txt", "w")

name = input("Enter your name: ")
age = input("Enter your age: ")
role = input("Enter your role: ")

file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Role: " + role + "\n")

file.close()

