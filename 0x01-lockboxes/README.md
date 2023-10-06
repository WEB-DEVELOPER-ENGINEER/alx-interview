# Lockboxes

## Project's name: 0x01. Lockboxes

## Tasks To Complete

+ [x] 0. **Lockboxes**<br/>[0-lockboxes.py](0-lockboxes.py) contains a function `def canUnlockAll(boxes):` that determines whether it is possible to unlock all the boxes in a list of boxes. Each box is represented as a list, and the function checks if you can navigate from the first box (index 0) to every other box by following the keys stored in each box. It uses a recursive algorithm to explore the contents of the boxes:
  + Returns `True` if all boxes can be unlocked, and `False` otherwise
  + You can assume all keys will be positive integers
  	+ There can be keys that do not have boxes
  + The first box boxes[0] is unlocked
