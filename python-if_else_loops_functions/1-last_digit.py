#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

Last_g = abs(number) % 10
if number < 0:
    Last_g = -Last_g

if Last_g > 5:
    print(f"Last_digit of {number} is {Last_g} and is greater than 5")

elif Last_g == 0:
    print(f"Last_digit of {number} is {Last_g} and is 0")

else:
    print(f"Last_digit of {number} is {Last_g} and is less than 6 and not 0")
