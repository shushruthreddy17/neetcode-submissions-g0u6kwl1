class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # sum -> number of ways to make that sum

        for num in nums:
            next_dp = {}

            for curr_sum, count in dp.items():
                # choose +num
                next_dp[curr_sum + num] = next_dp.get(curr_sum + num, 0) + count

                # choose -num
                next_dp[curr_sum - num] = next_dp.get(curr_sum - num, 0) + count

            dp = next_dp

        return dp.get(target, 0)