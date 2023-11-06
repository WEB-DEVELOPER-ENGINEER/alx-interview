#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    a method that determines if a given data set is a valid UTF-8 encoding
    """
    i = 0
    while i < len(data):
        if (data[i] & 0x80) == 0:
            i += 1
        elif (data[i] & 0xE0) == 0xC0:
            i += 1
            if i >= len(data) or (data[i] & 0xC0) != 0x80:
                return False
        elif (data[i] & 0xF0) == 0xE0:
            i += 1
            for j in range(2):
                if i >= len(data) or (data[i] & 0xC0) != 0x80:
                    return False
                i += 1
        elif (data[i] & 0xF8) == 0xF0:
            i += 1
            for j in range(3):
                if i >= len(data) or (data[i] & 0xC0) != 0x80:
                    return False
                i += 1
        else:
            return False

    return True
