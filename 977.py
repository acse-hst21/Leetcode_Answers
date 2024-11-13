class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                new_nums[i] = nums[r] ** 2
                r -= 1
            else:
                new_nums[i] = nums[l] ** 2
                l += 1
        return new_nums
        '''
        new_nums = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                new_nums.append(nums[r])
                r -= 1
            else:
                new_nums.append(nums[l])
                l += 1
        return [num*num for num in new_nums[::-1]]
        '''
