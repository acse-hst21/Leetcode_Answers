class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for index, word in enumerate(words):
            if searchWord in word and searchWord == word[0: len(searchWord)]:
                return index + 1
        return -1
