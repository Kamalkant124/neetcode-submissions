class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    self.dfs(board, r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
    def dfs(self, board, r, c):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != "O":
            return
        
        board[r][c] = "T"
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)