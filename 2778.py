class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[index]**2 for index in range(len(nums)) if len(nums)%(index+1) == 0)
