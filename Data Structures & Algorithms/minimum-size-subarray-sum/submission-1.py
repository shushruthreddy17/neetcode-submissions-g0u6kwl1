class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        left = 0
        min_length = 100001

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_length = min(min_length, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
        return 0 if min_length == 100001 else min_length

        