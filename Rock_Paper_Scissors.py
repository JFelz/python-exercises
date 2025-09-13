import random

while True:
    print("Welcome to the Rock, Paper, Scissors Tournament! Come test your luck.")
    player_choice = int(input("What do you choose? Type 0 for Rock, type 1 for Paper or 2 for Scissors?"))

    options = ["Rock", "Paper", "Scissors"]

    if 0 <= player_choice <= 2:
        print(f"You chose: {options[player_choice]}")
        computer_choice = random.randint(0, 2)
        print(f"Computer chose: {options[computer_choice]}")
        if player_choice == 0 and computer_choice == 2:
            print("You win!")
        elif player_choice == 2 and computer_choice == 1:
            print("You win!")
        elif player_choice == 1 and computer_choice == 0:
            print("You win!")
        elif player_choice == computer_choice:
            print("It\'s a draw!")
        else:
            print("You lose!")
    else:
        print("System error!")

    print("------------")