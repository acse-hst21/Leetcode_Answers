class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        counter = 0

        for index, _ in enumerate(s[:-1]):
            if s[index] !=s[index+1]:
                counter += 1
        
        return counter
