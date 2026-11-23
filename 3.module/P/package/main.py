from pathlib import Path

file_path = Path(__file__).parent / "info.txt"

def count_upper_digit_lower_in_info_file():
    with open(file_path, "r") as file:
        data = file.read()

    count_capitals = 0
    count_smalls = 0
    count_digits = 0
    
    for ch in data:
        if ch.isupper():
            count_capitals += 1
        elif ch.islower():
            count_smalls += 1
        elif ch.isdigit():
            count_digits += 1
            
    print("Capital char count =",count_capitals)
    print("Lower char count =", count_smalls)
    print("Digit count =", count_digits)
         
