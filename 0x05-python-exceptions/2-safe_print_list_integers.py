#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    while i < x:
        try:
            if type(my_list[i]) is not int:
                i += 1
                continue
            print(my_list[i], end="")
            count += 1
            i += 1
        except ValueError and TypeError:
            break
    print("")
    return i
