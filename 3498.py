class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((index+1) * (123 - ord(letter)) for index, letter in enumerate(s))
