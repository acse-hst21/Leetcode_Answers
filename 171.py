import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet_list = string.ascii_uppercase
        output = 0

        for index, char in enumerate(columnTitle[::-1]):
            output += (alphabet_list.index(char)+1) * (26**index)

        return output
        
        # one liner
        # return sum((string.ascii_uppercase.index(char)+1) * (26**index) for index, char in enumerate(columnTitle[::-1]))
