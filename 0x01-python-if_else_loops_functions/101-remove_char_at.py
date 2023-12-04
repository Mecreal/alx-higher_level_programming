#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    if (len(str) == 0 or len(str) < n):
        return (str)
    for i in range(len(str)):
        c = str[i]
        if i == n:
            continue
        else:
            new_str.append(c)
        result = ''.join(new_str)
    return (result)
