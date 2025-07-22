class Solution:
    def digitSum(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 10
            n //= 10
        return res
    def digitProduct(self, n: int) -> int:
        res = 1
        while n > 0:
            res *= n % 10
            n //= 10
        return res
    def checkDivisibility(self, n: int) -> bool:
        return n % (self.digitSum(n) + self.digitProduct(n)) == 0
