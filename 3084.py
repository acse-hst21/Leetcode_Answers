class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        output = 0
        for index in range(len(s)):
            if s[index] == c:
                output += s[index:].count(c)
        return output
