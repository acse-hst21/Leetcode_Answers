class Solution:
    def getSmallestString(self, s: str) -> str:
        s_copy = ''
        for index in range(len(s)-1):
            if int(s[index]) > int(s[index+1]) and (int(s[index])+int(s[index+1])) % 2 == 0:
                return s_copy + s[index+1] + s[index] + s[index+2:]
            else:
                s_copy += s[index]
        return s
