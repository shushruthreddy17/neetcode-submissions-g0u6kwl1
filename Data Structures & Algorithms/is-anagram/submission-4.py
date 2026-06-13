class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False
        count = defaultdict(int)

        for i in range(len_s):
            count[s[i]] += 1
            count[t[i]] -= 1
        
        for num, c in count.items():
            if c != 0:
                return False
        
        return True



