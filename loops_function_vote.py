# Author: Cold Id-deen
# Date: 10/3/2026
# Activity: Understand how comparision and if/elif/else applying to the functions and loops.

def greeting():
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}! ")
    return name 

def check_age(name):
    while True:
        menu = (
            f"Welcome to the Verification Age Vote System, {name}!\n"
            "______________________________________________________\n"
            "1. Verify yourself based on your age\n"
            
            "2. Exit the program\n"
        )
        print(menu)

        choice = input("Choose an option: ")

        if choice == "1":
            age = int(input("What is your age? "))

            if age < 18: 
                print("Too young...REJECTED!")
            elif 18 <= age < 50:
                print("You are eligible to vote!")
            elif 50 <= age < 70:
                print("Eh...okay, okay. You can vote, I guess so...")
            else:
                print("No way, you're too old! Lol.")

        elif choice == "2":
            print("Exiting the program...")
            break 
        else:
            print("Invalid choice! Please try again.")

name = greeting()
check_age(name)
