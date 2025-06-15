class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))

            perim = dfs(i, j+1)
            perim += dfs(i, j-1)
            perim += dfs(i+1, j)
            perim += dfs(i-1, j)

            return perim
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)
