#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lNum = int(repr(number)[-1])
if number < 0 :
    lNum *= -1

if (lNum > 5) :
    print(f"Last digit of {number} is {lNum} and is greater than 5")
elif (lNum == 0) :
    print(f"Last digit of {number} is {lNum} and is 0")
else :
    print(f"Last digit of {number} is {lNum} and is less than 6 and not 0")
