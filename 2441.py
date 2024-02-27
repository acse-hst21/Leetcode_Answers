class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        possible_values = []
        for num in nums:
            if num * -1 in nums:
                possible_values.append(num)
        if len(possible_values) == 0:
            return -1
        return max(possible_values)
