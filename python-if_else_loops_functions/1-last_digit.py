#!/usr/bin/python3
import, random.randint
number = random.randint(-10000, 10000)
a = number % 10
if str(number) [0] == "-":
    a = a-10
if a < 5:
    print("last digit of", number, "is", "and  is greather than 5")
elif a == 0:
    print("last digi of", number, "is", "and is 0")
elif a < 6 and a != 0:
    print("last digit of", number, "is", "and is less than 6 and not 0")
