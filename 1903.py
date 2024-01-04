class Solution:
    def largestOddNumber(self, num: str) -> str:
        num_letters_drop = 0
        for letter in num[::-1]:
            if int(letter) % 2 == 1:
                break
            num_letters_drop += 1
        return num[:len(num) - num_letters_drop]
