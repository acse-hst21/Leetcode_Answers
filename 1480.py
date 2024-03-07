class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        for index in range(1, len(nums)):
            output.append(output[index-1] + nums[index])
        return output
