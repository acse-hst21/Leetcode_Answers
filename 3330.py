class Solution:
    def possibleStringCount(self, word: str) -> int:
        consecutive_chars = sum(1 for index in range(len(word)-1) if word[index] == word[index+1])
        return consecutive_chars + 1
