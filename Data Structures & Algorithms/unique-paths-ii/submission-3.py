class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        for i in range(1,rows):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
                continue
            obstacleGrid[i][0] = obstacleGrid[i-1][0]
        
        for i in range(1,cols):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
                continue
            obstacleGrid[0][i] = obstacleGrid[0][i-1]
        
        for i in range(1,rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        
        return obstacleGrid[rows - 1][cols - 1]