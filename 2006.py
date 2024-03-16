class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        output = 0
        for num1 in nums:
            for num2 in nums:
                if abs(num1-num2) == k:
                    output += 1
        return int(output/2)
