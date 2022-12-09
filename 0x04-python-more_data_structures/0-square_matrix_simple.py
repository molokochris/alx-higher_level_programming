#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix_row = []
        for j in range(len(matrix)):
            new_matrix_row.append(matrix[i][j]**2)
        new_matrix.append(new_matrix_row)
    return new_matrix
