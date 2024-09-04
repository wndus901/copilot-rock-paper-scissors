# Write a rock, paper, scissors game
# import random module
import random

# define main funciton that handles all the logic
def main():
    # define the game choices
    choices = ['rock', 'paper', 'scissors']
    # define the game loop
    while True:
        # get the user choice
        user_choice = input('Choose rock, paper, or scissors: ')
        # get the computer choice
        computer_choice = random.choice(choices)
        # print the choices
        print(f'You chose {user_choice}, computer chose {computer_choice}')
        # determine the winner
        if user_choice == computer_choice:
            print('It\'s a tie!')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('You win!')
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You win!')
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('You win!')
        else:
            print('Computer wins!')
        # ask the user if they want to play again
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again != 'yes':
            break

# call the main function
main()