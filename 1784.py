class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s.rstrip('0')
        '''
        counter = 0
        for index in range(1, len(s)):
            if s[index-1] != s[index]:
                counter += 1
            if counter > 1:
                return False
        return True
        '''
