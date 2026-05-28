class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        for num in nums:
            if count == 0:
                count = 1
                majority = num
            elif num == majority:
                count += 1
            else:
                count -= 1

        return majority

        