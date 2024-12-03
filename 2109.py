class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ''
        spaces = set(spaces)
        for index in range(len(s)):
            if index in spaces:
                output += ' '
            output += s[index]
        return output
