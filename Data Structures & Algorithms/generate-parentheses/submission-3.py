class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, openN, closeN):
            if openN == closeN == n:
                res.append(cur)
            
            if openN < n:
                backtrack(cur + "(", openN + 1, closeN)
            
            if closeN < openN:
                backtrack(cur + ")", openN, closeN + 1)

        backtrack("", 0, 0)
        return res