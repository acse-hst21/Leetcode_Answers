from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [key for key in counter if counter[key] != 1]
