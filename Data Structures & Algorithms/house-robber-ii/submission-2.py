class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def robber(houses):
            rob1 = 0
            rob2 = 0

            for house in houses:
                temp = rob1
                rob1 = rob2 + house
                rob2 = max(temp, rob2)

            return max(rob1,rob2)
        
        if n == 1:
            return nums[0]
        
        return max(robber(nums[1:]), robber(nums[:-1]))