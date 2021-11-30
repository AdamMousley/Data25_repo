# def average(table):
#     if len(table) == 0:
#         return 0
#     else:
#         return sum(table)/len(table)
#
# table =[1,2,3,4,5]
# print(average(table))

# count the number of lower case "a" in a string

# def letter_a_counter(input):
#     list_a = 0
#     for letter in input:
#         if letter == "a":
#             list_a +=1
#     return list_a
#
# print(letter_a_counter("instagramaa"))

string = "Hello you!"
# def solution(string):
#     string = string.split(" ")
#     return string
#
# for i in solution(string):
#     print(i)

# arr = [0,1,2,3,4]
# arr = sorted(arr)
# print(arr)

# arr = [0,1,2,3,4]
# arr.append(5)
# print(arr)
#
# my_dict = {"Bob": "test", "Barry": "test2"}
# #print(my_dict.Bob != None)
#
# string_test=("adam")
#
# for c in list(string_test):
#     print(c)

# def closest_to_zero(ints):
#     pos_ints =[]
#     neg_ints = []
#     for i in ints:
#         if i > 0:
#             pos_ints.append(i)
#         else:
#             neg_ints.append(i)
#     pos_ints = sorted(pos_ints) # 1 to inf
#     neg_ints = sorted(neg_ints) # -inf to -1
#
#     if pos_ints[0] <= abs(neg_ints[-1]):
#         return pos_ints[0]
#     else:
#         return neg_ints[-1]
#
# values=[-122,22,-22,1,-1,3,4,-8]
# print(closest_to_zero(values))
# import math
# math.max(values)

import sys
import math
from contextlib import redirect_stdout
identification_number = 39847
def compute_check_digit(identification_number):
    sum_of_digits = 0
    for digits in str(identification_number):
        sum_of_digits += int(digits)
    print(sum_of_digits)



def main():
    identification_number = input()
    with redirect_stdout(sys.stderr):
        check_digit = compute_check_digit(identification_number)
    print(check_digit)
if __name__ == "__main__":
    main()




