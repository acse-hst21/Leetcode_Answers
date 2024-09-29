class Solution:
    def kthCharacter(self, k: int, word: str = 'a') -> str:
        while len(word) < k:
            new_word = ''.join([chr(ord(letter)+1) for letter in word])
            word += new_word
        return word[k-1]
