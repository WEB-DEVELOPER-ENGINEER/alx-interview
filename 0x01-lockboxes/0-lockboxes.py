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
    def dfs(box):
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key)
    dfs(0)
    return all(visited)
