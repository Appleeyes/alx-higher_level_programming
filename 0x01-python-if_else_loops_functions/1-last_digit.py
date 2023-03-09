#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = abs(number) % 10
if number < 0:
    lastNum = -lastNum
print(f"Last digit of {number:d} is {lastNum:d} and is ", end="")
if lastNum > 5:
    print("greater than 5")
elif lastNum == 0:
    print("0")
else:
    print("less than 6 and not 0")
