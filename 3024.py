class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if max(nums) >= (sum(nums)-max(nums)):
            return "none"
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 3:
            return "scalene"
        else:
            return "isosceles"
