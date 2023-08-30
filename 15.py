class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i == j or j == k or i == k:
                        pass
                    else:
                        if nums[i] + nums[j] + nums[k] == 0:
                            possible = [nums[i], nums[j], nums[k]]
                            possible = sorted(possible)
                            if possible not in output:
                                output.append(possible)
        
        return output
