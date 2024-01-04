class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_abs_value = 10000000
        for num in nums:
            if abs(num) < min_abs_value:
                min_abs_value = abs(num)
        if min_abs_value in nums:
            return min_abs_value
        return -1 * min_abs_value
