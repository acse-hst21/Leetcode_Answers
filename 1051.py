class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered_heights = sorted(heights)
        output = 0
        for a, b in zip(heights, ordered_heights):
            if a != b:
                output += 1
        return output
