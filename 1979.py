class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_value = min(nums)
        max_value = max(nums)

        for num in range(min_value, 0, -1):
            if max_value % num == 0 and min_value % num ==0:
                return num
