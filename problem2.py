## Problem2 (https://leetcode.com/problems/3sum/)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []
        
        for i in range(n):
            
            j = i + 1
            k = n - 1
            
            while j < k:
                
                if nums[i] + nums[j] + nums[k] == 0:
                    
                    if [ nums[i], nums[j], nums[k] ] not in output:
                        output.append( [ nums[i], nums[j], nums[k] ] )
                    j += 1
                    
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
                    
        return output
                
                