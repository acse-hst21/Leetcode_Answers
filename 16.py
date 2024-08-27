class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        output = float('inf')
        nums.sort()

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            
            l = index + 1
            r = len(nums) - 1

            while l < r:
                current_sum = nums[index] + nums[l] + nums[r]
                if current_sum == target:
                    return target
                if abs(current_sum-target) < abs(output-target):
                    output = current_sum
                    print(current_sum)
                if current_sum-target < 0:
                    l += 1
                else:
                    r -= 1
        
        return output
