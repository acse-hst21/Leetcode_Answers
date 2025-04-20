class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
                res += n
            else:
                n += 1
                n /= 2
                res += (n-1)
        return int(res)
