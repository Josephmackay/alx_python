#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = str(number)
la = n[-1]
last = int(la)
if last > 5:
    print("Last digit of", number, "is", last, "and is greater than 5")
elif last == 0:
    print("Last digit of", number, "is", last, "and is 0")
else:
    print("Last digit of", number, "is", last, "and is less than 6 and not 0")