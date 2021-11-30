# Question 1

import random

def find_largest(numbers):
    numbers.sort()
    return numbers[-1]

numbers = []
for i in range(1, 20):
    j = random.randint(1, 100)
    numbers.append(j)

print(numbers)
print(find_largest(numbers))
