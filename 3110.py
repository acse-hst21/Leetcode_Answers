class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[index+1]) - ord(s[index])) for index in range(len(s)-1))
