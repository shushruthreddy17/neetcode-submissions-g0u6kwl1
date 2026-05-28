class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in range(1,len(strs)):
                if i >= len(strs[s]) or strs[s][i] != char:
                    return strs[0][:i]
        return strs[0]
        