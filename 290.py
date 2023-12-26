class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.mask_pattern(pattern) == self.mask_s(s)
    
    def mask_pattern(self, pattern: str) -> List[int]:
        unique_letters = []
        mask = []

        for index, letter in enumerate(pattern):
            if letter not in unique_letters:
                unique_letters.append(letter)
                mask.append(index)
            else:
                mask.append(pattern.index(letter))
        
        return mask
    
    def mask_s(self, s: str) -> List[int]:
        s = s.split()
        unique_words = []
        mask = []

        for index, word in enumerate(s):
            if word not in unique_words:
                unique_words.append(word)
                mask.append(index)
            else:
                mask.append(s.index(word))
        
        return mask
