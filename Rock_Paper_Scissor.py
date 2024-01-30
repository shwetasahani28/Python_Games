import random

def play():
    while True:
        user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors \n(type 'exit' to end the game): ").upper()

        # .upper() is use so what both upper and lower case value can accepted.

        if user.lower() == 'exit':
            print("Thanks for playing! Exiting the game.")
            break

        computer = random.choice(['R', 'P', 'S'])

        if user not in ['R', 'P', 'S']:
            print("Invalid choice.\nPlease enter 'R', 'P', or 'S'.")
            continue

        if user == computer:
            print('It\'s a tie!')

        elif is_win(user, computer):
            print('You won!')

        else:
            print('You lost!')

# Function to define winning rules
def is_win(player, opponent):
    # r>s, s>p, p>r
    return (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R')

# Start the game
play() 

# either this [ play()] or this both same

# result = play()
# print(result)
