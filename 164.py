class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        max_value = 0

        for index, num in enumerate(nums):
            if index == 0:
                continue
            if abs(num - nums[index - 1]) > max_value:
                max_value = abs(num - nums[index - 1])
        return max_value
