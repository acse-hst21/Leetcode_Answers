from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        output = 0
        
        for key in counter:
            if key in jewels:
                output += counter[key]
        
        return output
