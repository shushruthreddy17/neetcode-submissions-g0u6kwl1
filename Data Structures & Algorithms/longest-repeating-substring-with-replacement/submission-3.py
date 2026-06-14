class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track = defaultdict(int)
        n = len(s)
        longest = 0
        left = 0
        res = 0

        for i in range(n):
            track[s[i]] += 1
            longest = max(longest, track[s[i]])

            while (i - left + 1) - longest > k:
                track[s[left]] -= 1
                left += 1
            
            res = max(res, i - left + 1)
        
        return res
                    