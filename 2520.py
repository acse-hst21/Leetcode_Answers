class Solution:
    def countDigits(self, num: int) -> int:
        output = 0
        for digit in str(num):
            if num % int(digit) == 0:
                output += 1
        return output
