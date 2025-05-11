from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        counter = Counter(words)
        for word in banned:
            del counter[word]
        return max(counter, key=counter.get)
