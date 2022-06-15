from datetime import *

try:
    year_of_birth = int(input("What is your year of birth?"))
    age = int(datetime.now().strftime("%Y")) - year_of_birth
except:
    print("Oops, there's an error in the code.")
    while True:
        try:
            year_of_birth = int(input("Enter your year of birth, using only figures."))
            if type(year_of_birth) == int:
                age = int(datetime.now().strftime("%Y")) - int(year_of_birth)
                print(f"You are {age} years old.")
                break
        except:
            print("Oh no, there's another error in the code!")  
else:
    print(f"You are {age} years old.")
