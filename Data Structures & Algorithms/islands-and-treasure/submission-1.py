class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # Gate found
                    self.dfs(grid, r, c, 0)
    
    def dfs(self, grid, r, c, dist):
        rows, cols = len(grid), len(grid[0])
        
        # Out of bounds or invalid cell or found a shorter distance
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] < dist or grid[r][c] == -1:
            return
        
        grid[r][c] = dist
        
        # Visit neighbors with dist + 1
        self.dfs(grid, r + 1, c, dist + 1)
        self.dfs(grid, r - 1, c, dist + 1)
        self.dfs(grid, r, c + 1, dist + 1)
        self.dfs(grid, r, c - 1, dist + 1)