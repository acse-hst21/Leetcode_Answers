class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        output = []
        for index in range(1, len(mountain) - 1):
            if mountain[index] > mountain[index - 1] and mountain[index] > mountain[index + 1]:
                output.append(index)
        return output
