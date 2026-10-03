# Author: Cold Id-deen
# Date: 10/3/2026
# Activity: Understand how comparision and if/elif/else applying to the functions.

# Create the function to check the age requirement
def check_voting_age(age):
    if age < 18:
        return "You are too young, rejected!"
    elif 18 <= age < 50:
        return "Okay, you can vote since you're older enough."
    elif 50 <= age < 70:
        return "Eh....I don't know but I guess you can vote."
    else:
        return "You are over 70, rejected."

# Ask the users for their age
age = int(input(" What's your age? "))
# Output the result with the age requirment
print(check_voting_age(age))
    