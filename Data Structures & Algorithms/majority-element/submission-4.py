class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                maj = nums[i]
                count = 1
            elif nums[i] == maj:
                count += 1
            else:
                count -= 1
        return maj