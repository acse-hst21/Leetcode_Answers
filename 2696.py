class Solution:
    def minLength(self, s: str) -> int:
        has_changed = True
        while has_changed:
            temp_s = s
            s = s.replace('AB', '')
            s = s.replace('CD', '')
            if temp_s == s:
                has_changed = False
        
        return len(temp_s)
