#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_number_list = []

    uniq_numbers = set(my_list)

    for number in uniq_numbers:
        uniq_number_list.append(number)
        addition_uniq = sum(uniq_number_list)

    return (addition_uniq)
