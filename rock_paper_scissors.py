import random

# Easier method: computer_choice = random.choice(['rock', 'paper', 'scissors'])

# Randomly generate computer's choice as a number
computer_choice_random = random.randrange(1, 4)

# Dictionary to map numbers to game choices
game_dictionary = {
    1: 'scissors',
    2: 'paper',
    3: 'rock'
}

# Get the computer's choice from the dictionary
computer_choice = game_dictionary.get(computer_choice_random)

# Prompt the user to input their choice
user_choice = input("What do you want to play rock, paper or scissors? ")

# Initialize the game result
win = True
Tie = False

# Strip any extra spaces from the user and computer choices
formatted_user_choice = user_choice.strip()
formatted_computer_choice = computer_choice.strip()

# Determine the result of the game
if formatted_user_choice == formatted_computer_choice:
    Tie = True
elif formatted_user_choice == "scissors" and formatted_computer_choice == "paper":
    pass
elif formatted_user_choice == "paper" and formatted_computer_choice == "rock":
    pass
elif formatted_user_choice == "rock" and formatted_computer_choice == "scissors":
    pass
else:
    win = False

# Print the choices
print("The user played " + formatted_user_choice + " and the machine played " + formatted_computer_choice)

# Print the result of the game
if Tie:
    print("This game is a tie!")
else:
    if win:
        print("Congratulations! You beat the machine")
    else:
        print("Better luck next time, the machine wins this one")