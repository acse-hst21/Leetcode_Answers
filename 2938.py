class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        output = 0

        for r in range(len(s)):
            if s[r] == '0':
                output += (r-l)
                l += 1
        
        return output
