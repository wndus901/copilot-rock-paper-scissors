# Write a rock, paper, scissors game
# import random module
import random

# define main funciton that handles all the logic
def main():
    # define the game choices
    choices = ['rock', 'paper', 'scissors', 'spock', 'lizard']
    winning_conditions = {
        'rock': ['scissors', 'lizard'],
        'scissors': ['paper', 'lizard', 'rock'],
        'paper': ['rock', 'spock'],
        'spock': ['rock', 'scissors'],
        'lizard': ['paper', 'spock']
    }
    # define the game loop using winning_condittions
    while True:
        # get the user choice
        user_choice = input('Choose rock, paper, scissors, spock, or lizard: ')
        # get the computer choice
        computer_choice = random.choice(choices)
        # print the choices
        print(f'You chose {user_choice}, computer chose {computer_choice}')
        # determine the winner
        if user_choice == computer_choice:
            print('It\'s a tie!')
        elif computer_choice in winning_conditions[user_choice]:
            print('You win!')
        else:
            print('Computer wins!')
        # ask the user if they want to play again
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again != 'yes':
            break


# call the main function
main()
# save the game result to a file
with open('/workspaces/copilot-rock-paper-scissors/game_results.txt', 'a') as file:
    file.write(f'User choice: {user_choice}, Computer choice: {computer_choice}\n')
    if user_choice == computer_choice:
        file.write('Result: Tie\n')
    elif computer_choice in winning_conditions[user_choice]:
        file.write('Result: User wins\n')
    else:
        file.write('Result: Computer wins\n')