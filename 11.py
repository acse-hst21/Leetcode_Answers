class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = 0
        l = 0
        r = len(height) - 1

        for _ in range(len(height)):
            area = min(height[l], height[r]) * abs(l-r)
            output = max(output, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return output
