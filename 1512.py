class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if index1 == index2:
                    pass
                else:
                    if nums[index1] == nums[index2]:
                        output += 1
        return int(output/2)
