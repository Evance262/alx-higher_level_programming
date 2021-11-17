#!/usr/bin/python3
def fizzbuzz():
    FIZZ = "Fizz"
    BUZZ = "Buzz"
    for number in range(1, 101):
        if (number % 3 and number % 5):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (number % 3):
            print("%s" % (FIZZ), end=' ')
        elif (number % 5):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (number), end=' ')
