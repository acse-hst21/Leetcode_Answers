class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper_case = set()
        lower_case = set()
        for char in word:
            if char.isupper():
                upper_case.add(char)
            else:
                lower_case.add(char)
        output = 0
        for char in lower_case:
            if char.upper() in upper_case:
                output += 1
        return output
