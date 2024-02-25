class Solution:
    def digitCount(self, num: str) -> bool:
        for index, digit in enumerate([*num]):
            if int(digit) == num.count(str(index)):
                pass
            else:
                return False
        return True
