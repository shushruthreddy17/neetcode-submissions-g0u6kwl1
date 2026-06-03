class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curMax, curMin = 0, 0

        maxSum = nums[0]
        minSum = nums[0]

        for num in nums:
            curMax = max(num, curMax + num)
            maxSum = max(maxSum, curMax)

            curMin = min(num, curMin + num)
            minSum = min(minSum, curMin)

        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)

        