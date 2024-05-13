# Tree Height Calculator

## Problem Description

Given a description of a rooted tree, the task is to compute the height of the tree. The height of a tree is defined as the maximum depth of any node, or the maximum distance from a leaf to the root.

## Approach

1. **Read the input:**
   - Read the number of nodes 𝑛.
   - Read the parent nodes of each node.

2. **Compute the height of the tree:**
   - Implement a depth-first search (DFS) algorithm to traverse the tree. DFS is often implemented using a stack data structure or recursion. But since recursion relies on the call stack, which can lead to stack overflow errors if the depth of recursion becomes too large; use an explicit stack data structure.
   - Initialize a list `heights` to store the height of each node, initialized with zeros.
   - Iterate over each node in the tree.
     - If the height of the current node is not zero, continue to the next node.
     - If the parent of the current node is -1, it's the root node, set its height to 1.
     - Otherwise, traverse upwards through the parent nodes until reaching a node whose height is already computed.
     - Set the height of the current node to the height of its parent plus 1.
   - Return the maximum height from the `heights` list.

3. **Output the height of the tree.**

## Sample Input and Output

- **Sample Input:**<br>
5<br>
4 -1 4 1 1<br>
- **Sample Output:**<br>
3

### Explanation

The input means that there are 5 nodes with numbers from 0 to 4:
- Node 0 is a child of node 4.
- Node 1 is the root.
- Node 2 is a child of node 4.
- Node 3 is a child of node 1.
- Node 4 is a child of node 1.

To visualize this, let's write the numbers of nodes from 0 to 4 in one line, and the numbers given in the input in the second line underneath:<br>
0 &nbsp;1 2 3 4<br>
4 -1 4 1 1<br>
Now we can see that node number 1 is the root because −1 corresponds to it in the second line. Also, nodes number 3 and number 4 are children of the root node 1. Also, nodes number 0 and number 2 are children of node 4.
