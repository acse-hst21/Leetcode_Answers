class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        counter = 0
        for index in range(len(nums)-2):
            if 2 * (nums[index]+nums[index+2]) == nums[index+1]:
                counter += 1
        return counter
