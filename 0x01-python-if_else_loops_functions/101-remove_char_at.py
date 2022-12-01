#!/usr/bin/python3
def remove_char_at(str, n):
    res = ' '
    for i in range(len(str)):
        if i != n:
            res += str[i]
    return res
