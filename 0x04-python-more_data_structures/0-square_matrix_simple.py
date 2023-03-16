#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x**2 if isinstance(x, int) else x for x in row] for row in matrix]
