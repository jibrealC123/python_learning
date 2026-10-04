# Author: Cold Id-deen
# Date: 10/3/2026
# Activity: Understand how comparison, if/elif/else statements,
# functions, and loops work together.


# Create a function to ask for the user's name and return the value.
def greeting():
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}! ")
    return name 


# Create a function that displays a menu with two options.
def check_age(name):
    while True:
        menu = (
            f"Welcome to the Verification Age Vote System, {name}!\n"
            "______________________________________________________\n"
            "1. Verify yourself based on your age\n"
            
            "2. Exit the program\n"
        )
        print(menu)

        # Ask the user to choose between the two menu options.
        choice = input("Choose an option: ")

        # Ask the user for their age if they choose option 1.
        if choice == "1":
            age = int(input("What is your age? "))

            # Use conditional statements to determine voting eligibility based on age.
            if age < 18: 
                print("Too young...REJECTED!")
            elif 18 <= age < 50:
                print("You are eligible to vote!")
            elif 50 <= age < 70:
                print("Eh...okay, okay. You can vote, I guess so...")
            else:
                print("No way, you're too old! Lol.")


                # The age conditions determine whether the user is eligible
                # based on the age entered.

        # Inform the user that the program is exiting if they choose option 2.
        elif choice == "2":
            print("Exiting the program...")
            break 

        # Inform the user that their choice is invalid if they enter
        # an option that is not listed in the menu.
        # The while loop then displays the menu again.
        else:
            print("Invalid choice! Please try again.")


# Call the greeting function and store the returned name.
name = greeting()

# Call the check_age function and pass the user's name to it.
check_age(name)