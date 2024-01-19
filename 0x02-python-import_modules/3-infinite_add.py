#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    a = 0
    for i in range(1, length):
        a += int(sys.argv[i])
    print(a)
