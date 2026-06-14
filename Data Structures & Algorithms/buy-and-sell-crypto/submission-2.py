class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left = 0
        for i in range(1,len(prices)):
            if prices[i] <= prices[left]:
                left = i
            else:
                maxprofit = max(maxprofit, prices[i] - prices[left])
        return maxprofit