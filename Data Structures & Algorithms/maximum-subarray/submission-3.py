class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxSub = nums[0]
        for num in nums:
            cur = max(num, cur + num)
            maxSub = max(cur, maxSub)
        return maxSub