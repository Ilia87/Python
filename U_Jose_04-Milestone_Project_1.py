## Creating function that takes in an input from user and returns the result in the correct data type

# def user_choice():
#     choice = 'WRONG'
#     within_range = False
#     while choice.isdigit() == False or within_range == False:
#
#         choice = input('Please enter a number (0-10): ')
#
#         if choice.isdigit() == False:
#             print('Sorry that is not a digit!')
#         if choice.isdigit() == True:
#             if int(choice) in range(10):
#                 within_range = True
#             else:
#                 print(f'Sorry {choice} is not in range (0-10)')
#                 within_range = False
#
#     print(int(choice))
#
#
# user_choice()


#### Simple User Interaction
#### Finally let's combine all of these ideas to create a small game
####  where a user can choose a "position" in an existing list and replace it with a value of their choice.
from IPython.core.display import clear_output



def display_game(game_list):
    print("Here is the current list")
    print(game_list)

def position_choice():
    choice = 'wrong'
    with_range = False
    while choice.isdigit() == False or with_range == False:
        choice = input('Pick a position to replace (0-4): ')
        if choice.isdigit() == False:
            print(f'Sorry "{choice}" is not a digit!')
        elif choice.isdigit() == True:
            if int(choice) in range(5):
                with_range = True
            else:
                print(f'Sorry "{choice}" is not a valid position (0-4)')
                within_range = False
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at the position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice ():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input('Keep playing (Y or N): ')
        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice == 'Y':
        return True
    else:
        return False


# Variable to keep game playing
game_on = True

# First Game List
game_list = [0,1,2,3,4]

while game_on == True:
    # Clear any historical output and show the game list
    clear_output()
    display_game(game_list)

    # Have player choose position
    position = position_choice()

    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)

    # Clear Screen and show the updated game list
    clear_output()
    display_game(game_list)

    # Ask if you want to keep playing
    game_on = gameon_choice()