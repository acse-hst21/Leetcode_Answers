class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        while True:
            if len(set(nums)) == len(nums):
                return counter
            counter += 1
            try:
                nums = nums[3:]
            except ValueError:
                return counter
