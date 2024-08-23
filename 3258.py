class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        output = 0
        for l in range(len(s)):
            for r in range(len(s)):
                if l > r:
                    pass
                else:
                    if s[l:r+1].count('1') <= k or s[l:r+1].count('0') <= k:
                        output += 1
        return output
