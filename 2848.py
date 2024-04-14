class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points_with_car = set()
        for start, end in nums:
            for point in range(start, end+1):
                points_with_car.add(point)
        return len(points_with_car)
