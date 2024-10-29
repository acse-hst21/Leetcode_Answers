from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        output = 0

        for word in counter1:
            if word in counter2:
                if counter1[word] == 1 and counter2[word] == 1:
                    output += 1
        
        return output

        # return sum(1 for word in words1 if words1.count(word)==1 and words2.count(word)==1)
