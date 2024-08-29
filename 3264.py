class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            current_index = nums.index(min(nums))
            nums[current_index] *= multiplier
        return nums
