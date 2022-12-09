#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = []
    for i in my_list:
        if i not in result:
            result.append(i)
        else:
            continue
    return sum(result)
