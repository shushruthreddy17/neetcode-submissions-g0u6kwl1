class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            used_days = 1
            cur_weight = 0

            for w in weights:
                if cur_weight + w > mid:
                    used_days += 1
                    cur_weight = 0

                cur_weight += w

            if used_days <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            