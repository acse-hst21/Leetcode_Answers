class Solution:
    def happyFunc(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = self.happyFunc(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
