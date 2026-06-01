class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nc < 0 or
                        nr >= rows or nc >= cols or
                        grid[nr][nc] != 2147483647
                    ):
                        continue

                    grid[nr][nc] = dist + 1
                    q.append((nr, nc))

            dist += 1
            