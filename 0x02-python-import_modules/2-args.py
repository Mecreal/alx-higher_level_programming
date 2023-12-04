#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    av = sys.argv
    ac = len(av) - 1
    if ac == 0:
        print("{:d} arguments.".format(ac))
    elif ac == 1:
        print("{:d} argument:".format(ac))
    else:
        print("{:d} arguments:".format(ac))
    for i in range(1, ac + 1):
        print("{:d}: {:s}".format(i, av[i]))
