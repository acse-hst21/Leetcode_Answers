class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        list_of_nums = ['0'*(4-len(str(num)))+str(num) for num in [num1, num2, num3]]
        output = 0
        for index in range(4):
            output += min(int(num[index]) for num in list_of_nums) * 10**(3-index)
        return output
