class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_occurences = len(nums) / 3
        
        output = []

        for value in nums:
            if nums.count(value) > min_occurences and value not in output:
                output.append(value)
        return output
