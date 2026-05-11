class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        length = len(prices)
        cur_min = prices[0]
        while i < length:
            if prices[i] > cur_min:
                profit += prices[i] - cur_min
            cur_min = prices[i]
            i += 1
        return profit
        