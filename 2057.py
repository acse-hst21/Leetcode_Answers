class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if nums[index] == index%10:
                return index
        return -1
