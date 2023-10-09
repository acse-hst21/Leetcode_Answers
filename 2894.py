class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for num in range(1, n + 1):
            if num % m == 0:
                num2 += num
            else:
                num1 += num
        return num1 - num2
