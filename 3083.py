class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for index in range(len(s)-1):
            if s[index] + s[index+1] in s[::-1]:
                return True
        return False
