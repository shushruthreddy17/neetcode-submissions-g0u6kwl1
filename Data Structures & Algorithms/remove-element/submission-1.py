class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        k = 0
        while i < n:
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1
                
        return k
        