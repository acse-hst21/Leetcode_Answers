class Solution:
    def counter(self, s: str) -> dict:
        counter = DefaultDict(int)
        for letter in s:
            counter[letter] += 1
        return counter
    def maxDifference(self, s: str) -> int:
        Counter = self.counter(s)
        
        even_counter = {key: Counter[key] for key in Counter if Counter[key]%2 == 0}
        odd_counter = {key: Counter[key] for key in Counter if Counter[key]%2 == 1}
        
        max_diff = max(odd_counter.values()) - min(even_counter.values())
        
        return max_diff
