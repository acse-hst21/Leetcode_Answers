class Solution:
    def removeZeros(self, n: int) -> int:
        return int(''.join([digit for digit in str(n) if digit != '0']))
