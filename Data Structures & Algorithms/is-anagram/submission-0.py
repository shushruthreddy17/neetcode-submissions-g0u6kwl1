class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        helper = [0]*26
        len_s, len_t= len(s), len(t)
        if len_s != len_t:
            return False
        for i in range(0,len_s):
            helper[ord(s[i]) - ord('a')] += 1
            helper[ord(t[i]) - ord('a')] -= 1
        
        for i in range(0,26):
            if helper[i] != 0:
                return False
        return True

        