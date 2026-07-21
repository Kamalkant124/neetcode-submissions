class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = collections.deque()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                self.addcell(grid, visited, queue, r + 1, c)
                self.addcell(grid, visited, queue, r - 1, c)
                self.addcell(grid, visited, queue, r, c + 1)
                self.addcell(grid, visited, queue, r, c - 1)
            dist += 1
    
    def addcell(self, grid, visited, queue, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == -1:
            return
        visited.add((r,c))
        queue.append([r,c])
        




        