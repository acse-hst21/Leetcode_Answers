class Solution:
    def isFascinating(self, n: int) -> bool:
        full_num = str(n) + str(2 * n) + str(3 * n)
        return len(set(full_num)) == len(full_num) and '0' not in full_num
