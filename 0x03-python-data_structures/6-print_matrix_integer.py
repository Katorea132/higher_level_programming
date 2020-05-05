#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{:d}'.format(i) for i in y]) for y in matrix]))
