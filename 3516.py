class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x) > abs(z-y):
            return 2
        elif abs(z-x) < abs(z-y):
            return 1
        else:
            return 0
        """
        d_one = abs(z-x)
        d_two = abs(z-y)
        distance_dict = {d_one: 1, d_two: 2}
        return distance_dict[min(d_one, d_two)] if d_one != d_two else 0
        """
