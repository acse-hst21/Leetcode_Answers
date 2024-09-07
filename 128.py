class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        output = 0

        for num in nums:
            if num-1 not in nums_set:
                current_length = 1
                while num+1 in nums_set:
                    current_length += 1
                    num += 1
                output = max(output, current_length)
        
        return output
