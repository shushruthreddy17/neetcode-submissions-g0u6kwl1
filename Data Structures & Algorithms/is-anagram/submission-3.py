class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0] * 26
        for i in range(len(s)):
            check[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            check[ord(t[i]) - ord('a')] -= 1
        for num in check:
            if num != 0:
                return False
        return True
        
        