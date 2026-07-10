class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            days_need = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > mid:
                    days_need += 1
                    current_load = 0
                current_load += weight
            if days_need > days:
                left = mid + 1
            else:
                right = mid - 1
        return left