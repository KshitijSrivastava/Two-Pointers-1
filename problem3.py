## Problem3 (https://leetcode.com/problems/container-with-most-water/)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        
        Maxwater = 0
        
        left = 0
        right = n - 1
        
        
        while left < right:
            
            water = min( height[left], height[right] ) * (right - left)
            
            Maxwater = max(Maxwater, water)
            
            if height[left] < height[right]:
                left += 1
            else:
                 right -= 1
        return Maxwater
            