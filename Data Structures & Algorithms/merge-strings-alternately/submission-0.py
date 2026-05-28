class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        s = []
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                s.append(word1[l])
                l += 1
            if r < len(word2):
                s.append(word2[r])
                r += 1
        return "".join(s)

        