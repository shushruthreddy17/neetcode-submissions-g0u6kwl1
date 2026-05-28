class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftmax = 0
        rightmax = 0
        total_water = 0

        while left < right:
            if height[left] <= height [right]:
                leftmax = max(leftmax, height[left])
                total_water += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                total_water += rightmax - height[right]
                right -= 1
            
        return total_water