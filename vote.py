# Author: Cold Id-deen
# Date: 10/3/2026
# Activity: Understand how comparision and if/elif/else works.

# Ask the user for their name and greet them.
name = input(" What is your name? ")
print(f" Nice to meet you, {name}! ")

# Inform the user about the age requirement.
print(" To vote, you must be at least 18 enough, you know that right? ")

# Ask the user for their age.
age = int(input(" What's your age? "))

# Check the user's age.
if age < 18:
    print(" You are too young, rejected. ")
elif 18 <= age < 50:
    print(" Ok....You can vote! ")
elif 50 <= age <= 70:
    print("Hm...okay. I guess you can vote, eh.")
else:
    print("You are over 70, rejected.")