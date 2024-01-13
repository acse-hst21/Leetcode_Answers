class Solution:
    def balancedStringSplit(self, s: str) -> int:
        letter_count = 0
        output = 0
        for letter in s:
            if letter == 'R':
                letter_count += 1
            else:
                letter_count -= 1
            if letter_count == 0:
                output += 1
        return output
