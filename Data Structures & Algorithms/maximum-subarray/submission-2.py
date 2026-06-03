class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxSub = nums[0]
        for num in nums:
            cur = cur + num
            maxSub = max(num, cur, maxSub)
            if cur < 0:
                cur = 0
        return maxSub