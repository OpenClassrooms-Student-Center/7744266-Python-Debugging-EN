from datetime import *

try:
    date_of_birth = int(input("What is your date of birth?"))
    age = int(datetime.now().strftime("%Y")) - date_of_birth
except:
    print("Oops, there's an error in the code.")
    while True:
        try:
            date_of_birth = int(input("Enter your date of birth, using only figures."))
            if type(date_of_birth) == int:
                age = int(datetime.now().strftime("%Y")) - int(date_of_birth)
                print(f"You are {age} years old.")
                break
        except:
            print("Oh no, there's another error in the code!")  
else:
    print(f"You are {age} years old.")
