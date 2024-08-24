class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            l = index + 1
            r = len(nums) - 1
            while l < r:
                current_sum = value + nums[l] + nums[r]
                if current_sum == 0:
                    output.append([value, nums[l], nums[r]])
                    l += 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return [list(x) for x in set(tuple(sublist) for sublist in output)]
