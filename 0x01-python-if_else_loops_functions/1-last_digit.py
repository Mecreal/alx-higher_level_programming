#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    last_dig = number % (-10)
else:
    last_dig = number % 10
print(f"Last digit of {number:d} is {last_dig:d}", end=' ')
if (last_dig == 0):
    print("and is 0")
elif (last_dig > 5):
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
