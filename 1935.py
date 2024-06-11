class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        valid_word_count = 0
        
        for word in words:
            if not any(letter in brokenLetters for letter in word):
                valid_word_count += 1
        
        return valid_word_count
