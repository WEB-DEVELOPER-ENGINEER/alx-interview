#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    func
    """
    if n < 1:
        return 0
    operations = 0
    clipboard = 0
    current_h = 1
    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
            operations += 1
        current_h += clipboard
        operations += 1
    return operations
