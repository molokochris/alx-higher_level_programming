#!/usr/bin/python3
for i in range(8):
    for ii in range(10):
        if (i == ii) or (i >= ii):
            continue
        else:
            print("{}{}".format(i, ii), end=', ')
print(89)
