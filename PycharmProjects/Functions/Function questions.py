print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

# def divisors(n: int) -> list:
#     i = 1
#     list = []
#     while i <= n:
#         if n % i == 0:
#             list.append(i)
#         i +=1
#     return(list)
# print(divisors(12))

#danny
def divisors2(number: int)->list:
    divisors_list= []
    for i in range(1,number+1):
        if number % i ==0:
            divisors_list.append(i)
    return divisors_list
print(f"danny {divisors2(12)}")

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function
# A1b:

# def factor(num1,num2):
#     if num1 % num2 == 0:
#         return True
#     elif num2 % num1 == 0:
#         return True
#     else:
#         return False
# print(factor(4,2))

#danny

def is_factor(num1: int, num2: int) -> bool:
    if num1 in divisors2(num2) or num2 in divisors2(num1):
        return True
    else:
        return False
print(f"danny {is_factor(4,6)}")

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
# numbers=[]
# letters ="abyz"
# for letter in letters:
#     number = ord(letter) - 96
#     numbers.append(number)
# print(numbers)
#
# def position(l: str):
#     return ord(l) - 96
# print(position("z"))

#danny
def alphabet_position(letter: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())
print("danny")
print(alphabet_position("C"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
ID=[]
def position(name: str):
    name = name.lower()
    for letter in name:
        number = ord(letter)-96
        ID.append(number)
    return ID
print(position("Adam"))

ID_final = ''.join(str(x) for x in ID)
print(ID_final)

#danny
def id_generator(name_string: str)->str:
    id = ""
    for letter in name_string:
        pos = alphabet_position(letter)
        id += str(pos)
    return id
print("danny")
print(id_generator("bob"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

ID_final = ''.join(str(x) for x in ID)
print(ID_final)

def password(numbers):
    result = 1
    value=[]
    for i in numbers:
        result = result * i
    return result
print(int(ID_final)-password(ID))

def password_generator(name_string: str) -> str:
    number = 0
    for i in id_generator(name_string):
        number += int(i)
    return str(int(id_generator(name_string))- number)
print(password_generator("bob"))
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# A3a:

# def prime(n: int):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for x in range(2,n):
#             if n % x == 0:
#                 return False
#         return True
# print(prime(11))

def is_prime(number) -> bool:
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False
    return prime

print(is_prime(11))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
# def prime(n):
#     if n != int(n):
#         print("Not an integer dummy, try again")
#     else:
#         if n == 1:
#             return False
#         elif n == 2:
#             return True
#         else:
#             for x in range(2,n):
#                 if n % x == 0:
#                     return False
#             return True
# print(prime(11.1))
def is_prime2(number) -> bool:
    if number.isdigit():
        prime = True
        for i in range(2,int(number)):
            if int(number) % i == 0:
                prime = False
        return prime
    else:
        print("please enter a digit")

# -------------------------------------------------------------------------------------- #
