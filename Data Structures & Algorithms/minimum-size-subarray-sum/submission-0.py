class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0

        # start with infinity because we want minimum
        min_len = float('inf')

        for right, num in enumerate(nums):

            # expand window
            window_sum += num

            # shrink while valid
            while window_sum >= target:

                # update answer
                min_len = min(min_len, right - left + 1)

                # shrink window
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len