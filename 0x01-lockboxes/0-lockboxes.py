#!/usr/bin/python3
'''a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    arr = []
    for i in range(len(boxes)):
        arr.append(i)
    arr.pop(0)
    val = boxes[0]
    return access(boxes, val, arr)


def access(boxes, val, arr):
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
