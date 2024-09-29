class Solution:
    def sumDigits(self, digit: int):
        output = 0
        while digit:
            output += digit % 10
            digit //= 10
        return output
    def minElement(self, nums: List[int]) -> int:
        return min(self.sumDigits(num) for num in nums)
