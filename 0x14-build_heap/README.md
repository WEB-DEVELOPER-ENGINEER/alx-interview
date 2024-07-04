# Heap Building Algorithm

## The why behind this algorithm

The first step of the HeapSort algorithm is to create a heap from the array you want to sort (HeapBuilding), HeapSort algorithm is a natural generalization of selection sort algorithm. Recall that in selection sort algorithms, we proceed as follows. Given an array, we first scan the whole array to find the maximum value. So, then we get this maximum value and swap it with the last element. Then, we forget about this last element and we can see that only n-1 first elements. Again, by scanning this array, we find the maximum value, and we swap it with the last element in this region, and so on. So, here in the heap sort algorithm, instead of finding the maximum value at each iteration, namely, we use a smart data structure, namely a binary heap. But there is a problem: we end up using some extra space for that smart data structure (binary heap). So here comes the role of building a heap; its role is to permute the elements of a given array so that the resulting array is actually a binary heap. Thus, it satisfies the binary heap property and is ready for the heap sort algorithm without the need for extra space, as we build the heap in place.

## Time Complexity

At first glance, the time complexity of `build_heap` appears to be O(n log n), as it consists of roughly n/2 calls to the SiftDown procedure, whose running time is log n. However, a more careful analysis reveals that the actual time complexity is O(n). For a detailed analysis, see: [University of California San Diego - Data Structures - Module 3 - Building a Heap](https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap)

## Input Format

- The first line contains a single integer n (the number of elements).
- The second line contains n space-separated integers ai (the elements of the array).

## Output Format

- The first line should contain a single integer m (the total number of swaps), where 0 ≤ m ≤ 4n.
- The next m lines should describe the swap operations used to convert the array 𝑎 into a heap, each represented by a pair of 0-based indices i, j of the elements to be swapped.

## Heap Property

After applying all swaps, the resulting array must satisfy the heap property, that is, for each 𝑖 where 0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:

1. If 2i + 1 ≤ n - 1, then ai < a2i+1
2. If 2i + 2 ≤ n - 1, then ai < a2i+2

## Example

Input: <br>
5 <br>
5 4 3 2 1 <br>
Output: <br>
3<br>
1 4<br>
0 1<br>
1 3<br>
### Explaination:
After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4. After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4. After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, which is already a heap, because 𝑎0 = 1 < 2 = 𝑎1, 𝑎0 = 1 < 3 = 𝑎2, 𝑎1 = 2 < 5 = 𝑎3, 𝑎1 = 2 < 4 = 𝑎4.
