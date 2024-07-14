class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_ones = s.count('1')
        string_ones = ''.join(['1' for x in range(count_ones-1)])
        string_zeros = ''.join(['0' for x in range(len(s)-count_ones)])
        return string_ones+string_zeros+'1'
