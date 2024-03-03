class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n+1):
            if '0' in str(num) + str(n-num):
                pass
            else:
                return [num, n-num]
