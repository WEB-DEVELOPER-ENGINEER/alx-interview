#!/usr/bin/python3

from collections import deque


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
    Args:
        boxes (list of lists): List of lists containing all
        the boxes (lists) with the keys.
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    queue = deque()
    queue.append(0)
    visited = set()
    visited.add(0)
    while queue:
        box_idx = queue.popleft()
        keys = boxes[box_idx]
        for key in keys:
            if key not in visited:
                queue.append(key)
                visited.add(key)
    return len(visited) == len(boxes)
