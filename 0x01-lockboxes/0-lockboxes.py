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
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited)
