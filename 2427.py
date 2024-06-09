class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        output = 0
        for num in range(1, min(a, b)+1):
            if a % num == 0 and b % num == 0:
                output += 1
        return output
