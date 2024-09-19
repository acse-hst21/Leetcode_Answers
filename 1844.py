class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ''
        for index in range(len(s)):
            if index % 2 == 0:
                output += s[index]
            else:
                new_letter = chr(ord(s[index-1]) + int(s[index]))
                output += new_letter
        return output
