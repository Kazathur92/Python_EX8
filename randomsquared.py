import random

nums = range(20)
random_numbers = []

for num in nums:
    random_numbers.append(random.randint(1, 50))

print(random_numbers)

