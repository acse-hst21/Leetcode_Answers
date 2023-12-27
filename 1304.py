class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        
        if n % 2 == 0:
            for num in range(1, n + 1):
                if num % 2 != 0:
                    output.append(num)
                else:
                    output.append(-1 * (num - 1))
        else:
            output = [0]
            for num in range(1, n):
                if num % 2 != 0:
                    output.append(num)
                else:
                    output.append(-1 * (num - 1))
        
        return output
