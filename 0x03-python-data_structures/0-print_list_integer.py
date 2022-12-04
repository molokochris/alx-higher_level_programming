#!/usr/bin/python3
def print_list_integer(my_list=[]):
    myString = "{}"
    for i in range(len(my_list)):
        print(myString.format(my_list[i]))
