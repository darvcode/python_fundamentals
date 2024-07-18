import random

def roll_dice():
    # Roll two six-sided dice and return their total
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():
    # Get player names
    player1 = input("Enter player 1's name:\n")
    player2 = input("Enter player 2's name:\n")

    # Roll dice for each player
    roll1 = roll_dice()
    roll2 = roll_dice()

    # Print the results of the rolls
    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    # Determine and print the winner
    if roll1 > roll2:
        print(player1, 'wins!')
    elif roll2 > roll1:
        print(player2, 'wins!')
    else:
        print('You tie!')

# Run the main function
main()
