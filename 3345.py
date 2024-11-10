class Solution:
    def digit_product(self, n: int) -> int:
        output = 1
        while n:
            output *= n % 10
            n //= 10
        return output
    def digit_prod(self, n: int) -> int:
        n = [*str(n)]
        output = 1
        for num in n:
            output *= int(num)
        return output
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if self.digit_product(n) % t == 0:
                return n
            n += 1
