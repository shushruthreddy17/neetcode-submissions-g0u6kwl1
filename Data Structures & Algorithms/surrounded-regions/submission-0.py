class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != "O"
            ):
                return
            
            board[r][c] = "T"

            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r+1,c)
        
        for i in range(rows):
            dfs(i,0)
            dfs(i,cols - 1)

        for i in range(cols):
            dfs(0, i)
            dfs(rows - 1, i)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        