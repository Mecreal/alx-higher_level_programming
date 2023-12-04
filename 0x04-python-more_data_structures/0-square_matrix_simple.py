#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    results = []
    for row in matrix:
        squared_row = list(map(lambda x: x ** 2, row))
        results.append(squared_row)
    return results
