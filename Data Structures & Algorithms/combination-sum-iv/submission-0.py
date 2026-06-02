class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [0] * (target+1)
        dp[0] = 1

        for total in range(target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]
        
        return dp[target]
