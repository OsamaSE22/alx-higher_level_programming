#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = list(map(lambda rwo: list(map(lambda x: x**2, rwo)), matrix))
    return result
