class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while True:
            if num == 0:
                return counter
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            counter += 1
