class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):

            # if already inside current window,
            # duplicate found within distance k
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            # keep window size at most k
            # remove element falling out of range
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False