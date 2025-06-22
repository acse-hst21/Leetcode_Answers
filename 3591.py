class Solution:
    def counter(self, nums: List[int]) -> dict:
        Counter = defaultdict(int)
        for num in nums:
            Counter[num] += 1
        return Counter
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        Counter = self.counter(nums)
        for value in Counter.values():
            if self.isPrime(value):
                return True
        return False
