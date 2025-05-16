class Solution:
    def counter(self, nums: List[int]) -> dict:
        output = DefaultDict(int)
        for num in nums:
            output[num] += 1
        final_output = {}
        for num in sorted(output):
            if num % 2 == 0:
                final_output[num] = output[num]
        return final_output
    def mostFrequentEven(self, nums: List[int]) -> int:
        Counter = self.counter(nums)
        try:
            return max(Counter, key=Counter.get)
        except ValueError:
            return -1
