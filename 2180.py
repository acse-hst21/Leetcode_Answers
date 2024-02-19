class Solution:
    def countEven(self, num: int) -> int:
        output = 0
        for number in range(1, num+1):
            digit_sum = 0
            for letter in str(number):
                digit_sum += int(letter)
            if digit_sum % 2 == 0:
                output += 1
        return output
