#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            results[i] = my_list_1[i] / my_list_2
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return results
