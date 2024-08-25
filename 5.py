class Solution: 
    def isPalindrome(self, s: str, l: int, r: int, output: str) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
                    if len(s[l:r+1]) > len(output):
                        output = s[l:r+1]
                    l -= 1
                    r += 1
        return output
    
    def longestPalindrome(self, s: str) -> str:
        output = ''
        
        for index in range(len(s)):
            output = self.isPalindrome(s, index, index, output)
            output = self.isPalindrome(s, index, index+1, output)
        
        return output
