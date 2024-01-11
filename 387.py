class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, letter in enumerate(s):
            if letter not in s[:index] + s[index + 1:]:
                return index        
        return -1
