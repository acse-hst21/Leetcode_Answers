class Solution:
    def pivotInteger(self, n: int) -> int:
        for num in range(1, n + 1):
            if sum(range(1, num + 1)) == sum(range(num, n + 1)):
                return num
        return -1
