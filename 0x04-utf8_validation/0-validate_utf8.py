#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    a method that determines if a given data set is a valid UTF-8 encoding
    """
    x = 0
    for num in data:
        if num <= 255:
            if x > 0:
                binary_repr = [int(bit) for bit in bin(num)[2:]]
                if len(binary_repr) == 8:
                    if binary_repr[0] != 1:
                        return False
                    if binary_repr[1] != 0:
                        return False
                    x -= 1
                else:
                    return False
            if num >= 127:
                binary_repr = [int(bit) for bit in bin(num)[2:]]
                for digit in binary_repr:
                    if digit == 0:
                        break
                    else:
                        x += 1
                if x > 4:
                    x = 0
        else:
            return False
    if x > 0:
        return False
    return True
