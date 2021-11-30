#number = 12345
# def getsum(n):
#     sumEven = 0
#     sumOdd = 0
#     number = str(n)
#     for digit in range(len(number)):
#         if (digit % 2 == 0):
#             sumOdd += int(number[digit])
#         else:
#             sumEven += int(number[digit])
#     sumEven = sumEven * 3
#     total = sumEven + sumOdd
#     lastdigit = int(str(total)[-1])
#     if lastdigit ==0:
#         return 0
#     else:
#         val = 10 - lastdigit
#         return val
#
#     # print(sumOdd)
#     # print(total)
#     # print(lastdigit)
#     # print(f"this is the final value {val}")
# getsum(39847)


#
# a_dict={"key":"test","key2":"test2"}
# for key, value in a_dict.items():
#     print(value)

def is_on_even_position(list_param, value):
    position = list_param.index(value)
    if position % 2 == 0:
        return True
    return False

print(str(is_on_even_position([4,6,8], 6)))


