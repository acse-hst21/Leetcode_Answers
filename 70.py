class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2

        output = 2
        counter = 2

        if n == n1:
            return 1
        elif n == n2:
            return 2
        else:
            while counter < n:
                output = n2 + n1
                n1 = n2
                n2 = output
                counter += 1
        return output
