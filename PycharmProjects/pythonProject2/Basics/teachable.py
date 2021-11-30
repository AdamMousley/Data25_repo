#Control Flow

# customer_age = 16
#
# if customer_age <= 12:
#     print('U, PG and 12 films available')
# elif customer_age <= 15:
#     print('U, PG, 12 and 15 films available')
# else:
#     print('All films available')

# time_of_Day = 6
#
# if time_of_Day > 5 and time_of_Day < 12:
#     print("Good morning")
# elif time_of_Day > 12 and time_of_Day <18:
#     print("Good Afternoon")
# else:
#     print("Good evening")

# passingScore = 65;
# studentScore = random.randint(0,100)
#
# if HERE:
#   testResult = True
# else:
#   testResult = False
#
# print(testResult)

import random

# game_random_number = random.randint(1,100)
# game_active = True
# while game_active:
#     game_start_message = "Guess a number between 1 - 100"
#     user_guess = int(input())
#     if user_guess == game_random_number:
#         print("You guessed correctly")
#         exit()
#     elif user_guess < game_random_number:
#         print("Too low, guess again")
#     else:
#         print("Too high, guess again")

# theList = getCustomers() # returns a list
# index = 0
# while index < len(theList):
# 	print( theList[index].getFirstName() )

def add(num1,num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2

choice = int(input('\n Enter 1 for addition or 2 for subtraction: '))

num1 = int(input('\n input your first number:'))
num2 = int(input('\n input your second number:'))

if choice == 1:
    print(num1, '+', num2, '=', add(num1,num2))
elif choice == 2:
    print(num1, '+', num2, '=', sub(num1,num2))
else:
    print("Invalid")



