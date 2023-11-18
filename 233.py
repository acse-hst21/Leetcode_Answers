class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        for num in range(n + 1):
            num_of_ones = str(num).count('1')
            ans += num_of_ones
        return ans
