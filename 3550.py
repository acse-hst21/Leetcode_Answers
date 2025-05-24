class Solution:
    def sumDigits(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 10
            n //= 10
        return res
    def smallestIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if self.sumDigits(num) == index:
                return index
        return -1
