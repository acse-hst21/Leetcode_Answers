class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[index-1] - nums[index]) for index in range(len(nums)))
