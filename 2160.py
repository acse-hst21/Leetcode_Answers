class Solution:
    def minimumSum(self, num: int) -> int:
        sorted_nums = sorted(str(num))
        return (int(sorted_nums[0]) + int(sorted_nums[1])) * 10 + int(sorted_nums[2]) + int(sorted_nums[3])
