#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b < 0:
        b *= -1
        for i in range(b):
            power = 1/(a * a)
    else:
        for i in range(b):
            power *= a

    return power
