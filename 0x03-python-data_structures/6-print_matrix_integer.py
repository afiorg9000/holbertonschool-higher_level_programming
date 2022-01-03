#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(' '.join([f"{i:3}" for i in row]))
