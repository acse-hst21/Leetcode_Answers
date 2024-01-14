class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        output = ''
        for word in s_list:
            output += word[::-1] + ' '
        return output[:-1]
