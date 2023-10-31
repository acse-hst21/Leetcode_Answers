class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s) + ['A']
        t = sorted(t)

        for s, t in zip(s, t):
            if s != t:
                return t
