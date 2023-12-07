#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s_s_t_w = 0
    s_w = 0
    for s, w in my_list:
        s_s_t_w = s_s_t_w + s * w
        s_w += w
    average = s_s_t_w/s_w
    return s_s_t_w