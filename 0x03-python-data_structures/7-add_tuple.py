#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        x_a = tuple_a[0]
        y_a = 0
    else:
        x_a, y_a = tuple_a[:2]
    if len(tuple_b) < 2:
        x_b = tuple_b[0]
        y_b = 0
    else:
        x_b, y_b = tuple_a[:2]
    tuple_c = (x_a + x_b, y_a + y_b)
    return tuple_c
