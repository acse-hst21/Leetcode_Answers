class Solution:
    def checkString(self, s: str) -> bool:
        different_letters = 0
        for index, letter in enumerate(s):
            if index == 0:
                if letter == 'b' and len(s) > 1 and 'a' in s:
                    return False
                else:
                    continue
            if letter != s[index - 1]:
                different_letters += 1
        
        if different_letters > 1:
            return False
        return True
