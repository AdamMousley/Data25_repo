list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]

class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


prime_numbers = []
for i in list_of_numbers:
    numbers = Number(i)
    if numbers.is_prime() == True:
        prime_numbers.append(i)
print(prime_numbers)


div_by_three_four = []
for z in list_of_numbers:
    numbers = Number(z)
    if numbers.divisible_by_n(3):
        if numbers.divisible_by_n(4):
            div_by_three_four.append(z)
print(div_by_three_four)


