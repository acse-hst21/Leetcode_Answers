class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(index-t.index(s[index])) for index in range(len(s)))
