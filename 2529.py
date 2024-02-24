class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_nums = 0
        negative_nums = 0
        for num in nums:
            if num > 0:
                positive_nums += 1
            elif num < 0:
                negative_nums += 1
        return max(positive_nums, negative_nums)
