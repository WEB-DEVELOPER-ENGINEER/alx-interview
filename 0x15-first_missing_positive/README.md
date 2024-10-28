# First Missing Positive

## Problem Description
Given an unsorted integer array `nums`, find the smallest positive integer that is missing from the array.

### Constraints
- **Time Complexity**: The algorithm must run in **O(n)** time.
- **Space Complexity**: The algorithm must use **O(1)**
- 1 <= nums.length <= 10^5
- 2^31 <= nums[i] <= 2^31 - 1

### Examples
Input: nums = [1, 2, 0] <br>
Output: 3 <br>
Explanation: The numbers in the range [1, 2] are all in the array.

## Solution Explanation
1. **Filter Out-of-Range Numbers**:
   - Iterate over `nums` and replace any number that is less than `1` or greater than `len(nums)` with a number outside the desired range (`len(nums) + 1`). This step simplifies the problem by allowing us to ignore irrelevant values.

2. **Mark Presence Using Hashing Technique**:
   - For each number in `nums`, treat its absolute value as an index. If a number `n` is within `[1, len(nums)]`, mark its corresponding index `n-1` in the array as visited by setting `nums[n-1]` to a negative value.
   - This marking serves as a "hash" to record which numbers in the range `[1, len(nums)]` are present without using extra space.

3. **Identify the Smallest Missing Positive**:
   - After marking, the first index `i` with a positive value indicates that the integer `i + 1` is missing. If all indices from `0` to `len(nums)-1` are negative, then all integers from `1` to `len(nums)` are present, so the answer is `len(nums) + 1`.
