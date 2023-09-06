class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        output = 0
        
        for index_1, value_1 in enumerate(nums):
            for index_2, value_2 in enumerate(nums):
                if index_1 == index_2:
                    pass
                else:
                    if value_1 + value_2 < target:
                        output += 1
        return int(output/2)
