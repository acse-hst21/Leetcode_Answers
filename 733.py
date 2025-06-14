class Solution:
    def neighbours(self, row: int, col: int, image: List[List[int]], start: int) -> List[Tuple[int, int]]:
        indices = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        return [(row, col) for row, col in indices if self.isValid(row, col, image) and image[row][col] == start]
    def isValid(self, row: int, col: int, image: List[List[int]]) -> bool:
        return row >= 0 and col >= 0 and row < len(image) and col < len(image[0])
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        queue = [(sr, sc)]
        visited = set()
        while len(queue) > 0:
            row, col = queue.pop(0)
            visited.add((row, col))
            image[row][col] = color
            for row, col in self.neighbours(row, col, image, start):
                if (row, col) not in visited:
                    queue.append((row, col))
        return image
