class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        total_nums = list(nums1) + list(nums2) + list(nums3)
        output = []

        for num in total_nums:
            if total_nums.count(num) >= 2:
                output.append(num)
        
        return list(set(output))
