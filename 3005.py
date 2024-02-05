from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_value = max(Counter(nums).values())
        output = 0

        for value in Counter(nums).values():
            if value == max_value:
                output += max_value
        
        return output
