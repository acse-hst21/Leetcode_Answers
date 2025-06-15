class Solution:
    def neighbours(self, row: int, col: int, grid: List[List[str]]) -> List[Tuple[int, int]]:
        indices = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        return [(row, col) for row, col in indices if self.isValid(row, col, grid) and grid[row][col] == '1']

    def isValid(self, row: int, col: int, grid: List[List[str]]) -> bool:
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))
            while len(queue) > 0:
                row, col = queue.popleft()
                for row, col in self.neighbours(row, col, grid):
                    if (row, col) not in visited:
                        queue.append((row, col))
                        visited.add((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands
