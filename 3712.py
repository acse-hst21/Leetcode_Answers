class Solution:
    def counter(self, nums: List[int]) -> dict:
        Counter = defaultdict(int)
        for num in nums:
            Counter[num] += 1
        return Counter
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        Counter = self.counter(nums)
        return sum(key * value for key, value in Counter.items() if value%k == 0)
