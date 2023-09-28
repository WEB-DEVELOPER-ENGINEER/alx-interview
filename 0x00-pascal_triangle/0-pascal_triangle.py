#!/usr/bin/python3
'''a function that returns a list of lists of integers representing 
the Pascal’s triangle of n'''


def pascal_triangle(n):
    Arr = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = Arr[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        Arr.append(row)
    return Arr
