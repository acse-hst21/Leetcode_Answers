import numpy as np
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid = np.array(grid)
        my_list = grid.flatten()

        counter = Counter(my_list)
        repeated_num = counter.most_common(1)[0][0]
        for num in range(1, len(my_list) + 1):
            if num not in my_list:
                missing_num = num
                return [repeated_num, missing_num]
