class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        index = 0
        while index < len(nums):
            if nums[index] != 1:
                index += 1
                continue
            if 1 in nums[index+1:index+1+k]:
                return False
            index += k
        return True
