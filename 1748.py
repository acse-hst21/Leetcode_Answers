from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        output= 0
        counter = Counter(nums)
        for key in counter:
            if counter[key] == 1:
                output += key
        return output
