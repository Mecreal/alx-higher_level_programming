#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print(my_list[i], end="")
                count += 1
        except ValueError and TypeError:
            break
    print("")
    return i
