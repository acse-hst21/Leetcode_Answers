import numpy as np

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        binary_list = []
        for value in range(len(nums)):
            binary_list.append(bin(value))
        
        index_list = []

        for value in binary_list:
            if value.count('1') == k:
                index_list.append(1)
            else:
                index_list.append(0)

        nums = np.array(nums)
        index_list = np.array(index_list)

        output = np.sum(nums * index_list)

        return output
