class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        output = ''
        for word in s.split()[::-1]:
            output += word
            output += ' '
        return output[:-1]
