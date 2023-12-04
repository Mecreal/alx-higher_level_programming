#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    av = sys.argv
    ac = len(av) - 1
    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    dic = {'+': add, '-': sub, '/': div, '*': mul}
    if av[2] not in list(dic.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(av[1])
    b = int(av[3])
    print("{} {} {} = {}".format(a, av[2], b, dic[av[2]](a, b)))
