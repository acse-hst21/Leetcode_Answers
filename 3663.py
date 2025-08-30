class Solution:
    def counter(self, n: int) -> dict:
        Counter = defaultdict(int)
        for digit in self.digitsInNum(n):
            Counter[digit] += 1
        return Counter
    def digitsInNum(self, n: int) -> List[int]:
        res = []
        while n:
            last_digit = n % 10
            res.append(last_digit)
            n //= 10
        return res
    def getLeastFrequentDigit(self, n: int) -> int:
        counter = self.counter(n)
        return min(counter, key=lambda x: (counter[x], x))
