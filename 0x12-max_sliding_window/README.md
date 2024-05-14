# Maximum in Sliding Window

## Problem Introduction
Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1. A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately. Design an 𝑂(𝑛) algorithm.

## Problem Description
**Input Format:** 
- The first line contains an integer 𝑛.
- The second line contains 𝑛 integers 𝑎1, . . . , 𝑎𝑛 separated by spaces.
- The third line contains an integer 𝑚.

**Output Format:** 
max{𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.

## Example
**Input:**

8

2 7 3 1 5 2 6 2

4

**Output:**

7 7 5 6 6

## Solution Description
Store relevant items in a dequeue. Use a double-ended queue (dequeue) to store elements of the current window. At the same time, store only relevant elements: before adding a new element drop all smaller elements.
