#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    j = -1 * (-number % 10)
else:
    j = number % 10
if j > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, j))
elif j == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, j))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, j))
