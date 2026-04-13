class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, sum):
            if sum == target:
                res.append(list(curr))
                return
            
            if i == len(candidates) or sum > target:
                return

            # Include the current element
            curr.append(candidates[i])
            dfs(i+1,curr, sum+candidates[i])
            curr.pop()
            
            # Skip duplicates: find the next unique element
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            dfs(next_i,curr, sum)

        dfs(0,[],0)

        return res