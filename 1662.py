class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word = ''
        second_word = ''

        for word in word1:
            first_word += word
        for word in word2:
            second_word += word
        
        if first_word == second_word:
            return True
        return False
