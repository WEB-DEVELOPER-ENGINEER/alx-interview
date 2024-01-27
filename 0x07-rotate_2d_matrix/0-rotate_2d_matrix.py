#!/usr/bin/python3
"""
Script to rotate 2d matrix
"""

def rotate_2d_matrix(matrix):
    """
        function to rotate 2d matrix
    """
    y = len(matrix)
    x = len(matrix[0])
    mat = []
    arr = []

    for i in range(0, x):
        for n in range(y - 1, -1, -1):
            arr.append(matrix[n][i])
        mat.append(arr)
        arr = []
    for i in range(0, y):
        matrix[i] = mat[i]
    return
