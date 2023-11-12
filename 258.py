class Solution:
    def addDigits(self, num: int) -> int:
        num_as_str = str(num)
        while len(num_as_str) > 1:
            sum_digits = 0
            for value in num_as_str:
                sum_digits += int(value)
            num_as_str = str(sum_digits)
        
        return int(num_as_str)
