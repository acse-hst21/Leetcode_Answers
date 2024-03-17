class Solution:
    def generateTheString(self, n: int) -> str:
        output = ''
        if n % 2 == 0:
            output += (n-1) * 'a'
            output += 'b'
        else:
            output += n * 'a'
        return output
