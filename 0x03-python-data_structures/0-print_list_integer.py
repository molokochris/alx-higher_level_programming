#!/usr/bin/python3
def print_list_integer(my_list=[]):
    str = "{}"
    for i in range(len(my_list)):
        print(str.format(my_list[i]))
