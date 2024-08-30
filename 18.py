class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1

                while l < r:
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if current_sum == target:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                    elif current_sum < target:
                        l += 1
                    else:
                        r -= 1
            
        return [x for x in set(tuple(sublist) for sublist in output)]
