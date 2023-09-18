class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        counter = 0
        for _ in range(len(nums)):
            if nums == sorted(nums):
                return counter
            else:
                nums.insert(0, nums[-1])
                nums.pop(-1)
                counter += 1
        return -1
