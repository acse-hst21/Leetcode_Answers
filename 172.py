class Solution:
    def trailingZeroes(self, n: int) -> int:
        output = 0
        while n >= 5:
            n //= 5
            output += n
        return output
