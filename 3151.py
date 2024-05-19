class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for index in range(len(nums) - 1):
            if nums[index] % 2 == nums[index+1] % 2:
                return False
        return True
