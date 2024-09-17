from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter((s1 + ' ' + s2).split(' '))
        return [key for key in counter if counter[key] == 1]
