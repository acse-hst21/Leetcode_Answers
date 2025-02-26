class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while True:
            if len(s) == 2:
                return s[0] == s[1]
            new_s = ''
            for index in range(len(s)-1):
                new_s += str((int(s[index]) + int(s[index+1])) % 10)
            s = new_s
