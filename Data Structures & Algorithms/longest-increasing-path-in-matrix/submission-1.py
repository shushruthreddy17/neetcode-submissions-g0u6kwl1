class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            best = 1

            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    best = max(best, 1 + dfs(nr, nc))
                
            dp[(r,c)] = best
            return best

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r,c))
            
        return longest