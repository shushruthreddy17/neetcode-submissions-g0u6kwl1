class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = 0, 0
        for i in range(len(cost)):
            cost[i] = cost[i] + min(a,b)
            a, b = b, cost[i]
        return min(cost[n-1], cost[n-2])