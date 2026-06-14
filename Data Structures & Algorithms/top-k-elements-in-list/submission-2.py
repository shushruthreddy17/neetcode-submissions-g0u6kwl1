class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            bucket[c].append(num)
        
        res = []
        for i in range(n,0,-1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res