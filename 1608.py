class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for num in range(len(nums)+1):
            count = sum(1 for number in nums if number >= num)
            if count == num:
                return num
        return -1
