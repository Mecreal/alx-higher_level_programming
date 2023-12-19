#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for chara in my_string:
        if chara != 'c' and chara != 'C':
            new_str = new_str + chara
    return new_str
