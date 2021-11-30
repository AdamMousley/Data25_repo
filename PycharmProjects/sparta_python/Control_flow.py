#Control flow exercise

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
# print(x[:5])
#
# i=0
# while i < 5:
#     print(x[i])
#     i +=1
# Dannys way
counter = 1
for number in x:
    if counter <= 5:
        print(number)
        counter += 1

print("\nQ1b\n")
# # Q1b: Now print only the even numbers in this list (the elements that are themselves even)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
# i = 0
# while i < len(x):
#     if x[i] % 2 == 0:
#         print(x[i])
#     i += 1

# Danny work
for number in x:
    if number % 2 == 0:
        print(number)


print("\nQ1c\n")
# # Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# i = 0
# while i < 5:
#     if x[i] % 2 == 0:
#         print(x[i])
#     i += 1

# Danny
counter = 1
for number in x:
    if counter > 5:
        break
    elif number % 2 == 0:
        print(number)
    counter += 1



print("\nQ2a\n")
# # Q2a: from the list of names, create another list that consists of only the first letters of each first name
# # e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
first_initial = []
for name in names:
    first_initial.append(name[:1])
print(first_initial)

print("\nQ2b\n")
# # Q2b: from the list of names, create another list that consists of only the index of the space in the string
# # HINT: use your_string.index("substring")
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
# #names.index("substring")
#
# names2 = []
# my_string = " "
# for name in names:
#     my_string = my_string + ' ' + name
# print(my_string.strip())

space_index = []
for name in names:
    space_pos = name.index(" ")
    space_index.append(space_pos)
print(space_index)

print("\nQ2c\n")
# # Q2c: from the list of names, create another list that consists of the first and last initial of each individual
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
# names2=[]
# # for name in names:
# #         names.split(" ")
# #         names2.append(name[0])
# #         print(names2)
# names=list(names[0])
# print(names)

initials = []
for name in names:
    first_initial = name[0]
    second_initial = name[name.index(" ") + 1]
    initials.append(first_initial + second_initial)
print(initials)

#Danny
initials = []
for name in names:
    initials.append(name[0:1] + name[(name.index(" ")+1):(name.index(" ")+2)])
print(initials)

print("\nQ3a\n")
# # Q3a: Here is a list of lists, print only the lists which have no duplicates
# # Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
no_duplicates = []
for item in list_of_lists:
    if len(item) == len(set(item)): # Danny used len instead of sorted
        no_duplicates.append(item)
print(no_duplicates)


# print("\nQ4a\n")
# # Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# # get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# # they entered

# guessing = True
# while guessing:
#     start_message = "Guess a number over 100:"
#     print(start_message)
#     num1 = int(input())
#     if num1 < 100:
#         print("Guess higher")
#     else:
#         print("Completed")
#         break

#Danny
user_prompt = True
while user_prompt:
    number = input("Please type in a number that is greater than 100... ")
    if number.isdigit():
        if int(number) >= 100:
            user_prompt = False
print(number)


print("\nQ4b\n")
# # Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# guessing = True
# while guessing:
#     start_message = "Guess a number over 100:"
#     print(start_message)
#     num1 = int(input())
#     if num1 < 100:
#         print("Guess higher")
#     else:
#         print("Completed")
#         break
# print("Enter a value:")
# user_input = int(input())

# user_input = 101
# print()
# while user_input <= 100:
#     print(f'youndlwieufhe {user_input}')
#     break
#
# if user_input > 100:
#     for n in range(2, user_input):
#         if (user_input % n) == 0:
#             print("it's not a prime number")
#             break
#     else:
#        print("It's a prime number ")


user_prompt = True
while user_prompt:
    number = input("Please type in a number that is greater than 100...")
    if number.isdigit():
        if int(number) >= 100:
            user_prompt = False
prime = True
for i in range(2, int(number)):
    if int(number) % i == 0:
        prime = False
if prime:
    print("Prime")
else:
    print("Not prime")
