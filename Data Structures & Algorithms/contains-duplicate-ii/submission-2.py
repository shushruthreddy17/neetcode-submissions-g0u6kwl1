class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                check.remove(nums[left])
                left += 1
            
            if nums[right] in check:
                return True
            
            check.add(nums[right])
            
        return False


        