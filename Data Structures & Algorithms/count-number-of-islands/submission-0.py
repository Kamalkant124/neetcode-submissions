class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count_islands = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.dfs(grid, r, c, visited):
                    count_islands += 1
        
        return count_islands
    
    def dfs(self, grid, r, c, visited):

        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])):
            return False
        
        if (r,c) in visited:
            return False
        
        if grid[r][c] == "0":
            return False

        visited.add((r,c))

        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r, c - 1, visited)
        self.dfs(grid, r, c + 1, visited)

        return True

        