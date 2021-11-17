#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ldigit = number % 10
else:
    ldigit = ((number * -1) % 10) * -1

msg = "Last digit of %d is %d and is" % (number, ldigit)

if ldigit == 0:
    print(msg, "0")
elif ldigit > 5:
    print(msg, "greater than 5")
else:
    print(msg, "less than 6 and not 0")
