class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = [x for x in range(left, right + 1)]
        for num in range(left, right + 1):
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    output.remove(num)
                    break
        return output
