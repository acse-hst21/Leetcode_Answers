from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_number = -1
        counter = Counter(arr)
        for key, value in zip(counter.keys(), counter.values()):
            if key == value and key > lucky_number:
                lucky_number = key
        return lucky_number
