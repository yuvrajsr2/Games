import random

user_input = input("Rock, Paper, Scissors shoot: ")
random_choice = random.choice(("Rock", "Paper", "Scissors"))

if user_input == random_choice:
    print("Tie")
    print("You: " + user_input)
    print("Computer: " + random_choice)

elif user_input == "Rock" and random_choice == "Paper":
    print("Computer won")
    print("You: " + user_input)
    print("Computer: " + random_choice)

elif user_input == "Paper" and random_choice == "Rock":
    print("You won")
    print("You: " + user_input)
    print("Computer: " + random_choice)

elif user_input == "Rock" and random_choice == "Scissors":
    print("You won")
    print("You: " + user_input)
    print("Computer" + random_choice)

elif user_input == "Paper" and random_choice == "Scissors":
    print("Computer Won")
    print("You:" + user_input)
    print("Computer: " + random_choice)
