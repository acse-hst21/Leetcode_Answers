class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        current_dis = 10000
        index = 0
        for i, point in enumerate(points):
            if x != point[0] and y != point[1]:
                pass
            else:
                man_dis = abs(x-point[0]) + abs(y-point[1])
                if man_dis < current_dis:
                    current_dis = man_dis
                    index = i
        if current_dis == 10000:
            return -1
        return index
