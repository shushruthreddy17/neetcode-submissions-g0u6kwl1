class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,num in enumerate(nums):
            req = target - num
            if req in prevmap:
                return [prevmap[req], i]
            prevmap[num] = i


        