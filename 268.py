class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for value in range(0, len(nums)+1):
            if value not in nums:
                return value
