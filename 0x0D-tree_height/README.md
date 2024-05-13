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
0 &nbsp1 2 3 4<br>
4 -1 4 1 1<br>
Now we can see that node number 1 is the root because −1 corresponds to it in the second line. Also, nodes number 3 and number 4 are children of the root node 1. Also, nodes number 0 and number 2 are children of node 4.
