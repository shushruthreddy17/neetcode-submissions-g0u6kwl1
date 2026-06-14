class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        longest = 0
        for num in nums:
            count = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest