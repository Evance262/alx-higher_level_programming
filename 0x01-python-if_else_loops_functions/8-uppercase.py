#!/usr/bin/python3
def convert(letter):
    if ord(letter) >= 97 and ord(letter) <= 123:
        return (ord(letter) - 32)
    else:
        return (ord(letter))

def uppercase(str):
    new_str = ""
    for letter in str:
        new_str += "%c" % convert(letter)
    print("{:s}".format(new_str))
