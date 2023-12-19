#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    x_a, y_a, x_b, y_b = (0, 0, 0, 0)
    if len(tuple_a) == 1:
        x_a = tuple_a[0]
    elif len(tuple_a) >= 2:
        x_a, y_a = tuple_a[:2]
    if len(tuple_b) == 1:
        x_b = tuple_b[0]
    elif len(tuple_b) >= 2:
        x_b, y_b = tuple_b[:2]
    tuple_c = (x_a + x_b, y_a + y_b)
    return tuple_c
