class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed_num = int(str(num)[::-1])
        return int(str(reversed_num)[::-1]) == num
