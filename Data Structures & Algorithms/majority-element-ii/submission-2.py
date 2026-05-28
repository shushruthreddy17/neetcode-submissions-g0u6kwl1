class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1 = maj2 = None
        count1 = count2 = 0

        for num in nums:

            if num == maj1:
                count1 += 1

            elif num == maj2:
                count2 += 1

            elif count1 == 0:
                maj1 = num
                count1 = 1

            elif count2 == 0:
                maj2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        res = []

        if nums.count(maj1) > len(nums) // 3:
            res.append(maj1)

        if maj2 != maj1 and nums.count(maj2) > len(nums) // 3:
            res.append(maj2)

        return res