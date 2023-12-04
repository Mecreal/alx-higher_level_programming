#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_cp = a_dictionary.copy()
    for k, v in a_dictionary.items():
        dict_cp[k] *= 2
    return (dict_cp)
