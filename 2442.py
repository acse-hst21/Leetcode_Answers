class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_nums = []
        for num in nums:
            new_nums.append(int(str(num)[::-1]))
        nums += new_nums
        return len(set(nums))
