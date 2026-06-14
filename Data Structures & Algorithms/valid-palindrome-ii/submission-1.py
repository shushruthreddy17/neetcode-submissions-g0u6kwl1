class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s):
            left, right = 0, len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return valid(s[left+1:right+1]) or valid(s[left:right])
            left += 1
            right -= 1
        return True