class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        maxVol = 0
        right = len(heights)-1
        while left < right:
            dist = right - left
            if heights[left] <= heights[right]:
                currentVol = heights[left] * dist
                left += 1
            else:
                currentVol = heights[right] * dist
                right -= 1
            maxVol = max(maxVol, currentVol)
        return maxVol
            
        