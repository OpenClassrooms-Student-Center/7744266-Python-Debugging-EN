def sayGoodMorningOrGoodAfternoon(numberOfTimes, name):
    choice = input("Type 1 to say good morning and 2 to say good afternoon")
    if choice == "1":
        i = 0
        while i < numberOfTimes:
            print(f"Good morning {name}")
            i = i + 1
    elif choice == str(2):
        for i in range(0, numberOfTimes):
            print(f"Good evening {name}")
    else:
        print("I didn't understand your choice")

sayGoodMorningOrGoodAfternoon(5, "Bob")
