class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [index for index, num in enumerate(sorted(nums)) if num == target]
