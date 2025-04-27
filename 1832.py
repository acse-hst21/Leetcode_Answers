import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = string.ascii_lowercase
        return set(sentence) == set(alphabet)        
