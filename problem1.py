
## Problem1 (https://leetcode.com/problems/sort-colors/)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        k = 0
        
        for v in [0,1,2]:
            if v in d:
                for i in range(d[v]):
                    nums[k] = v
                    k += 1
        