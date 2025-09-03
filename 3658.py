class Solution:
    def gcd(self, num1: int, num2: int) -> int:
        divisor = min(num1, num2)
        for num in range(divisor, 0, -1):
            if num1 % num == 0 and num2 % num == 0:
                return num
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum = sum(num for num in range(1, n+1)) * 2
        odd_sum = even_sum - n
        return self.gcd(even_sum, odd_sum)
