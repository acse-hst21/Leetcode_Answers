class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        max_ones = 1
        current_ones = 1
        for index in range(len(nums)-1):
            if nums[index] == 1 and nums[index+1] == 1:
                current_ones += 1
            else:
                current_ones = 1
            if current_ones > max_ones:
                max_ones = current_ones
        return max_ones
