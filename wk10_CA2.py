# def display_list(mylist):
#     print(mylist)

# mylist = [0,1,2,3,4,5,6,7,8,9,10]
# display_list(mylist)


# result = input("Please enter a number: ")

# print(result)

# print(type(result))

# print(int(result))





# def user_choice():
#     '''
#     User inputs a number (0-10) and we return this in integer form.
#     No parameter is passed when calling this function.
#     '''
#     choice = input("Please input a number (0-10):")

#     return int(choice)

# print(type(user_choice()))



# some_input = '10'

# # Lot's of .is methods availble on string
# print(some_input.isdigit())



# def user_choice():

#     # This original choice value can be anything that isn't an integer
#     choice = 'wrong'

#     # While the choice is not a digit, keep asking for input.
#     while choice.isdigit() == False:

#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input("Choose a number: ")

#     # We can convert once the while loop above has confirmed we have a digit.
#     return int(choice)

# user_choice()




# def user_choice():

#     # This original choice value can be anything that isn't an integer
#     choice = 'wrong'

#     # While the choice is not a digit, keep asking for input.
#     while choice.isdigit() == False:

#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input("Choose a number: ")

#         # Error Message Check
#         if choice.isdigit() == False:
#             print("Sorry, but you did not enter an integer. Please try again.")

#     # We can convert once the while loop above has confirmed we have a digit.
#     return int(choice)

# user_choice()



# def user_choice():

#     # This original choice value can be anything that isn't an integer
#     choice = 'wrong'

#     # While the choice is not a digit, keep asking for input.
#     while choice.isdigit() == False:

#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input("Choose a number: ")

#         # Error Message Check
#         if choice.isdigit() == False:
#             print("Sorry, but you did not enter an integer. Please try again.")

#     # We can convert once the while loop above has confirmed we have a digit.
#     return int(choice)

# user_choice()

# from IPython.display import clear_output
# clear()

# def user_choice():

#     # This original choice value can be anything that isn't an integer
#     choice = 'wrong'

#     # While the choice is not a digit, keep asking for input.
#     while choice.isdigit() == False:

#         # we shouldn't convert here, otherwise we get an error on a wrong input
#         choice = input("Choose a number: ")

#         if choice.isdigit() == False:
#             # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
#             clear_output()

#             print("Sorry, but you did not enter an integer. Please try again.")

#     # Optionally you can clear everything after running the function
#     # clear_output()

#     # We can convert once the while loop above has confirmed we have a digit.
#     return int(choice)

# user_choice()




# from os import system, name 
# # define our clear function 
# def clear(): 
#     # for windows 
#     if name == 'nt': 
#         _ = system('cls') 
#     # for mac and linux(here, os.name is 'posix') 
#     else: 
#         _ = system('clear') 
# def user_choice():
#     '''
#     User inputs a number (0-10) and we return this in integer form.
#     No parameter is passed when calling this function.
#     '''
#     choice = 'wrong'
#     while choice.isdigit() == False:
#         choice = input("Choose a number: ")
#         # Error Message Check
#         if choice.isdigit() == False:
#             clear()
#             print("Sorry, but you did not enter an integer. Please try again.")
#     return int(choice)
# user_choice()



# def display_board(board):
#     clear()

# print





from os import system, name 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def user_choice():
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")
        # Error Message Check
        if choice.isdigit() == False:
            clear()
            print("Sorry, but you did not enter an integer. Please try again.")
    return int(choice)
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
user_choice()
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)



# from os import system, name 
# # define our clear function 
# def clear(): 
#     # for windows 
#     if name == 'nt': 
#         _ = system('cls') 
#     # for mac and linux(here, os.name is 'posix') 
#     else: 
#         _ = system('clear') 
# def user_choice():
#     '''
#     User inputs a number (0-10) and we return this in integer form.
#     No parameter is passed when calling this function.
#     '''
#     choice = 'wrong'
#     while choice.isdigit() == False:
#         choice = input("Choose a number: ")
#         # Error Message Check
#         if choice.isdigit() == False:
#             clear()
#             print("Sorry, but you did not enter an integer. Please try again.")
#     return int(choice)



# def display_board(board):
#     clear()
#     print('   |   |')
#     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('   |   |')
# user_choice()
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)







from os import system, name 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def user_choice():
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    choice = 'wrong'
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Choose one of these numbers (0-10): ")
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        if choice.isdigit():
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False
    clear()
    return int(choice)
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
user_choice()
test_board = ['#','#','#','X','O','X','O','X','O','X']
display_board(test_board)