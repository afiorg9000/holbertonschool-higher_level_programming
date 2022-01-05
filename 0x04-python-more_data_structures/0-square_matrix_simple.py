#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in range(len(matrix)):
        r = []
        for j in range(len(matrix[i])):
            r.append(matrix[i][j]**2)
        m.append(r)
    return m
