class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rhs_sum = sum(nums)
        lhs_sum = 0
        for index in range(len(nums)):
            if lhs_sum == rhs_sum - nums[index]:
                return index
            lhs_sum += nums[index]
            rhs_sum -= nums[index]
        return -1
