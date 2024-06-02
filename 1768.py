from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        for letter1, letter2 in zip_longest(word1, word2, fillvalue=''):
            output += letter1 + letter2
        return output
