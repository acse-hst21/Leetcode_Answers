class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for index, value in enumerate(gain):
            altitudes.append(altitudes[index] + value)
        return max(altitudes)
