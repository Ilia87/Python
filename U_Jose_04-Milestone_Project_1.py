# Creating function that takes in an input from user and returns the result in the correct data type

def user_choice():
    choice = 'WRONG'
    within_range = False
    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number (0-10): ')

        if choice.isdigit() == False:
            print('Sorry that is not a digit!')
        if choice.isdigit() == True:
            if int(choice) in range(10):
                within_range = True
            else:
                within_range = False

    print(int(choice))


user_choice()