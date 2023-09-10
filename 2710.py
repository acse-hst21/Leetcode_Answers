class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != '0':
            return num
        num_reverse = num[::-1]
        counter = 0
        for value in num_reverse:
            if value != '0':
                break
            counter += 1
        return num[:-(counter)]
