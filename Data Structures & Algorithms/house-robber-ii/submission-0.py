class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            prev = 0
            curr = 0

            for money in arr:
                temp = max(curr, prev + money)
                prev = curr
                curr = temp

            return curr

        return max(
            rob_line(nums[:-1]),  # exclude last house
            rob_line(nums[1:])    # exclude first house
        )