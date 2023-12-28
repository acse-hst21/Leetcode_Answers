class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = [*magazine]

        for letter in ransomNote:
            try:
                magazine.remove(letter)
            except ValueError:
                return False
        
        return True
