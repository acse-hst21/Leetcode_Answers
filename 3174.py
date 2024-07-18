class Solution:
    def clearDigits(self, s: str) -> str:
        output = ''
        digit_counter = 0
        for value in s[::-1]:
            try:
                a = int(value)
                digit_counter += 1
                continue
            except ValueError:
                pass
            if digit_counter:
                digit_counter -= 1
            else:
                output += value
        return output[::-1]
