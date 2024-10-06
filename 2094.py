class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = []
        for index1 in range(len(digits)):
            for index2 in range(len(digits)):
                for index3 in range(len(digits)):
                    if digits[index3] % 2 != 0 or digits[index1] == 0:
                        continue
                    if index1 == index2 or index2 == index3 or index1 == index3:
                        continue
                    
                    num1 = str(digits[index1])
                    num2 = str(digits[index2])
                    num3 = str(digits[index3])
                    
                    output.append(int(num1+num2+num3))
        return list(sorted(set(output)))

'''
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = set()
        for permutation in permutations(digits, 3):
            if permutation[0] != 0 and permutation[2] % 2 == 0:
                num = permutation[0]*100 + permutation[1]*10 + permutation[2]
                output.add(num)
        return sorted(output)
'''
