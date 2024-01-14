from math import log

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        log_value = log(n, 2)
        if abs(int(log_value) - log_value) < 0.000000000001:
            return True
        return False
