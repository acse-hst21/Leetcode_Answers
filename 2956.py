class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = 0
        num2 = 0

        for num in nums1:
            if num in nums2:
                num1 += 1
        for num in nums2:
            if num in nums1:
                num2 += 1
        
        return [num1, num2]
