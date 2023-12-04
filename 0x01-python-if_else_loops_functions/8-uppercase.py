#!/usr/bin/python3
def uppercase(string):
    new_str = []
    if (len(string) == 0):
        print("".format())
        return
    for i in range(len(string)):
        c = string[i]
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            new_str.append(chr(ord(c) - 32))
        else:
            new_str.append(c)
        result = ''.join(new_str)
    print("{}".format(result))
