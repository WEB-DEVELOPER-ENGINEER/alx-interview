#!/usr/bin/python3
'''a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
    Args:
        boxes (list of lists): List of lists containing all
        the boxes (lists) with the keys.
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    arr = []
    for i in range(len(boxes)):
        arr.append(i)
    arr.pop(0)
    val = boxes[0]
    return access(boxes, val, arr)


def access(boxes, val, arr):
    """A helper function that recursively unlocks boxes.
    It operates on a single box at a time,
    checking its keys to unlock other boxes.
    Args:
        boxes (list of lists): List of lists containing all
        the boxes (lists) with the keys.
        val (list): The box (list) that we are currently checking its keys.
        arr (list): A list containing the numbers of boxes.
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(arr) == 0:
        return True
    if len(val) != 0:
        for x in val:
            if x in arr:
                arr.remove(x)
                value = boxes[x]
                access(boxes, value, arr)
    if len(arr) == 0:
        return True
    return False
