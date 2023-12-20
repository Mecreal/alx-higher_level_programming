#!/usr/bin/python3

def safe_print_integer(value):
    try:
        test = 1 + value
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
