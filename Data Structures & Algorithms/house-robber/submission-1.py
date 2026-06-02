class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = rob1
            rob1 = num + rob2
            rob2 = max(temp, rob2)
        return max(rob1, rob2)