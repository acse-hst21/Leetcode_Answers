class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s_copy = ''
        for index in range(len(s)):
            s_copy += s[(k+index) % len(s)]
        return s_copy
