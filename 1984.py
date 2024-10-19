class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff = max(nums)
        for i in range(len(nums)-k+1):
            diff = abs(nums[i] - nums[i+k-1])
            min_diff = min(min_diff, diff)
        return min_diff
        
        '''
        nums.sort()
        sub_arrays = [nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1) if j-i==k]
        return min(abs(array[0]-array[-1]) for array in sub_arrays if len(array)==k)
        '''
