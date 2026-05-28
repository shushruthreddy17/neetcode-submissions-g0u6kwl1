class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set()

        for num in nums:
            check.add(num)

        longest = 0
        for num in nums:
            if num - 1 not in check:
                count = 0
                curr = num
                while curr in check:
                    count += 1
                    curr = curr + 1
                longest = max(longest, count)
        return longest
        