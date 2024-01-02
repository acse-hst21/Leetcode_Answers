class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        output = 0
        for word in words:
            if s.startswith(word):
                output += 1
        return output
