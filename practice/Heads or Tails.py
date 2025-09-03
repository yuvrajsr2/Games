# Import random to randomize the output
import random

# List that has heads and tails and we will use in select
output = ["heads", "tails"]

# Using random.choice to find out the output either heads or tails
select = random.choice(output)

# Getting user's choice
user = input("heads or tails: ")

# If user and select is same then
if user == select:
    print("You won, " + select + " won")
else:
    print("You lost, " + select + " won")