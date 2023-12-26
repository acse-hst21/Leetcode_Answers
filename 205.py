class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.mask(s) == self.mask(t)
    
    def mask(self, text: str) -> List[int]:
        unique_letters = []
        mask = []
        for index, letter in enumerate(text):
            if letter not in unique_letters:
                mask.append(index)
                unique_letters.append(letter)
            else:
                mask.append(unique_letters.index(letter))
        return mask
