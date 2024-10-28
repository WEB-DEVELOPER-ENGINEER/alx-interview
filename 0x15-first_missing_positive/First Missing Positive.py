class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = length + 1
        for i in range(length):
            num = abs(nums[i])
            if 1 <= num <= length:
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1