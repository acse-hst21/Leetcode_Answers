class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index_row = 0
        count = 0
        for index, row in enumerate(mat):
            if row.count(1) > count:
                count = row.count(1)
                index_row = index
        return [index_row, count]
