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
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
