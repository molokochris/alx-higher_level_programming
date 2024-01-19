#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv)-1))
        for arg in range(1, len(sys.argv)):
            print("{}: {}".format(arg, sys.argv[arg]))
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("0 arguments.")
