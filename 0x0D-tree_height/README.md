# Tree Height Calculator

## Problem Description

Given a description of a rooted tree, the task is to compute the height of the tree. The height of a tree is defined as the maximum depth of any node, or the maximum distance from a leaf to the root.

## Approach

1. **Read the input:**
   - Read the number of nodes 𝑛.
   - Read the parent nodes of each node.

2. **Compute the height of the tree:**
   - Start from the root node.
   - Traverse the tree, keeping track of the depth of each node.
   - Return the maximum depth encountered during the traversal.

3. **Output the height of the tree.**

## Sample Input and Output

- **Sample Input:**<br>
5<br>
-1 0 4 0 3<br>
- **Sample Output:**<br>
4
