class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if abs(index1 - index2) >= indexDifference and abs(value1 - value2) >= valueDifference:
                    return [index1, index2]
        return [-1, -1]
