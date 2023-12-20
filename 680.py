class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                drop_right = s[left:right]
                drop_left = s[left+1:right+1]
                return drop_right == drop_right[::-1] or drop_left == drop_left[::-1]
            left = left + 1
            right = right - 1
        return True
