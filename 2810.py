class Solution:
    def finalString(self, s: str) -> str:
        output = ''
        for value in s:
            if value == 'i':
                output = output[::-1]
            else:
                output += value
        return output
