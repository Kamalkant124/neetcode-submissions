class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific, atlantic = set(), set()

        for c in range(COLS):
            self.dfs(heights, 0, c, pacific, heights[0][c])
            self.dfs(heights, ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            self.dfs(heights, r, 0, pacific, heights[r][0])
            self.dfs(heights, r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res

    def dfs(self, heights, r, c, visited, prevHeight):

        if (r, c) in visited or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]) or heights[r][c] < prevHeight:
            return
        visited.add((r,c))

        self.dfs(heights, r + 1, c, visited, heights[r][c])
        self.dfs(heights, r - 1, c, visited, heights[r][c])
        self.dfs(heights, r, c + 1, visited, heights[r][c])
        self.dfs(heights, r, c - 1, visited, heights[r][c])